from django.db import models, transaction
from simple_history.models import HistoricalRecords
from productos.models import Producto
from django.contrib.auth.models import User

class Venta(models.Model):
    METODOS_PAGO = [
        ('EF', 'Efectivo'),
        ('TC', 'Tarjeta Crédito'),
        ('TD', 'Tarjeta Débito'),
        ('TR', 'Transferencia'),
        ('OT', 'Otro'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ventas')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    metodo_pago = models.CharField(max_length=2, choices=METODOS_PAGO, default='EF')
    anulada = models.BooleanField(default=False)
    mixto_efectivo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Cash portion for OT
    mixto_otros = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    # Non-cash portion for OT
    history = HistoricalRecords()

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"

    def save(self, *args, **kwargs):
        # Ensure mixto fields are only set for OT, null for others
        if self.metodo_pago != 'OT':
            self.mixto_efectivo = None
            self.mixto_otros = None
        super().save(*args, **kwargs)

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"

    def calcular_subtotal(self):
        self.subtotal = self.producto.precio * self.cantidad

    def save(self, *args, **kwargs):
        self.calcular_subtotal()
        super().save(*args, **kwargs)

class Caja(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='cajas')
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    esta_abierta = models.BooleanField(default=True)
    history = HistoricalRecords()

    def __str__(self):
        estado = 'Abierta' if self.esta_abierta else 'Cerrada'
        return f"Caja #{self.id} - {self.usuario.username} ({estado})"

class MovimientoCaja(models.Model):
    TIPO_CHOICES = [
        ('INGRESO', 'Ingreso'),
        ('EGRESO', 'Egreso'),
    ]

    caja = models.ForeignKey(Caja, on_delete=models.CASCADE, related_name='movimientos')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.tipo} ${self.monto} - {self.descripcion[:20]}"

@transaction.atomic
def procesar_venta(venta, detalles_venta):
    """
    Actualiza el stock y guarda los detalles de venta,
    además actualiza el total de la venta.
    """
    total = 0
    for detalle in detalles_venta:
        producto = detalle.producto
        if producto.stock < detalle.cantidad:
            raise ValueError(f"No hay stock suficiente para {producto.nombre}")
        producto.stock -= detalle.cantidad
        producto.save()

        detalle.venta = venta
        detalle.save()

        total += detalle.subtotal

    venta.total = total
    venta.save()

@transaction.atomic
def revertir_venta(venta, usuario_actual, motivo=None):
    if venta.anulada:
        raise ValueError("La venta ya fue anulada.")

    caja_abierta = Caja.objects.filter(usuario=usuario_actual, esta_abierta=True).last()
    if not caja_abierta:
        raise ValueError("No hay una caja abierta para registrar la anulación.")

    for detalle in venta.detalles.all():
        producto = detalle.producto
        producto.stock += detalle.cantidad
        producto.save()

    venta.anulada = True
    venta.anulada_por = usuario_actual
    venta.motivo_anulacion = motivo
    venta.save()

    MovimientoCaja.objects.create(
        caja=caja_abierta,
        tipo='EGRESO',
        monto=venta.total,
        descripcion=f"Anulación de venta #{venta.id} - {motivo if motivo else 'Sin motivo especificado'}"
    )

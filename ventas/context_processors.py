from decimal import Decimal
from django.db.models import Sum
from .models import Caja

def saldo_caja_actual(request):
    if request.user.is_authenticated:
        caja = Caja.objects.filter(usuario=request.user, esta_abierta=True).first()
        if caja:
            ingresos = caja.movimientos.filter(tipo='INGRESO').aggregate(total=Sum('monto'))['total'] or Decimal('0.00')
            egresos = caja.movimientos.filter(tipo='EGRESO').aggregate(total=Sum('monto'))['total'] or Decimal('0.00')
            saldo = caja.saldo_inicial + ingresos - egresos
            return {'saldo_caja_actual': saldo}
    return {'saldo_caja_actual': None}

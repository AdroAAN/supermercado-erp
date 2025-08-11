# ventas/admin.py
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Venta, DetalleVenta

@admin.register(Venta)
class VentaAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'fecha', 'total', 'metodo_pago', 'anulada')

@admin.register(DetalleVenta)
class DetalleVentaAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'venta', 'producto', 'cantidad', 'subtotal')

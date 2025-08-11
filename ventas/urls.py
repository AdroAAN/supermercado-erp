from django.urls import path
from . import views
from .views import obtener_info_producto, get_stock, producto_info

app_name = 'ventas'

urlpatterns = [
    path('', views.lista_ventas, name='lista_ventas'),
    path('crear/', views.crear_venta, name='crear_venta'),
    path('editar/<int:pk>/', views.editar_venta, name='editar_venta'),
    path('anular/<int:pk>/', views.anular_venta, name='anular_venta'),
    path('ventas/<int:venta_id>/', views.detalle_venta, name='detalle_venta'),
    path('ventas/<int:venta_id>/export_pdf/', views.export_venta_pdf, name='export_venta_pdf'),
    path('ventas/export_excel/', views.export_ventas_excel, name='export_ventas_excel'),
    path('ventas/reportes/', views.reporte_ventas, name='reporte_ventas'),
    path('venta/<int:venta_id>/ticket/', views.ticket_venta, name='ticket_venta'),
    
    # Endpoint para obtener info de producto POR ID (usado en get_stock, etc)
    path('api/producto-info-id/', obtener_info_producto, name='obtener_info_producto'),
    
    # Endpoint para obtener info de producto POR NOMBRE (para búsquedas)
    path('api/producto-info/', producto_info, name='producto_info_nombre'),
    
    path('ventas/<int:venta_id>/historial/', views.historial_venta, name='historial_venta'),
    path('productos/get_stock/<int:producto_id>/', get_stock, name='ventas_get_stock'),
    path('ventas/<int:venta_id>/comparar/<int:version_a>/<int:version_b>/', views.comparar_historial_venta, name='comparar_historial_venta'),
    path('venta/<int:venta_id>/ticket/data/', views.ticket_venta_data, name='ticket_venta_data'),
    
    # Control de Caja
    path('caja/abrir/', views.abrir_caja, name='abrir_caja'),
    path('caja/cerrar/', views.cerrar_caja, name='cerrar_caja'),
    path('caja/estado/', views.estado_caja_actual, name='estado_caja_actual'),
    path('caja/movimientos/', views.movimientos_caja, name='movimientos_caja'),
]
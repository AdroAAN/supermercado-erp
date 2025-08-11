from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # URLs para gestión de usuarios
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:pk>/desactivar/', views.desactivar_usuario, name='desactivar_usuario'),
    path('usuarios/<int:pk>/reactivar/', views.reactivar_usuario, name='reactivar_usuario'),
    path('usuarios/exportar-excel/', views.exportar_usuarios_excel, name='exportar_usuarios_excel'),

    # URLs para restablecer contraseña con vistas personalizadas
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

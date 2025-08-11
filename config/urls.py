from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from reportes import views as reportes_views   # ← import para root-dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    # ---------- apps propias ----------
    path('ventas/',    include('ventas.urls')),
    path('productos/', include('productos.urls', namespace='productos')),
    path('compras/',   include('compras.urls')),            # <- la crearás luego
    path('reportes/',  include('reportes.urls')),           # <- sólo UNA vez
    path('accounts/',  include('accounts.urls')),
    path('historial/', include('historial.urls')),

    # ---------- auth ----------
    path('login/',  auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),         name='logout'),

    # ---------- raíz: redirige al dashboard ----------
    path('', reportes_views.dashboard, name='dashboard'),   # sin namespace duplicado
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

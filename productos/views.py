from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods, require_POST
from django.templatetags.static import static
from .models import Producto, Categoria
from .forms import ProductoForm

# Decorador personalizado
def grupo_requerido(*nombres_grupos):
    def decorador(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name__in=nombres_grupos).exists():
                return view_func(request, *args, **kwargs)
            from django.contrib import messages
            from django.shortcuts import redirect
            messages.error(request, "No tienes permisos para acceder a esta sección.")
            return redirect('reportes:dashboard')  # Ajusta si tu dashboard es diferente
        return _wrapped_view
    return decorador

@grupo_requerido('Encargado', 'Gerente')
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/productos_list.html', {'productos': productos})

@grupo_requerido('Encargado', 'Gerente')
@require_POST
def crear_categoria(request):
    nombre = request.POST.get('nombre', '').strip()
    descripcion = request.POST.get('descripcion', '').strip()
    if not nombre:
        return JsonResponse({
            'success': False,
            'html': '<div class="bg-red-600 text-white p-3 rounded mb-4">El nombre es obligatorio.</div>'
        })
    cat = Categoria.objects.create(nombre=nombre, descripcion=descripcion)
    return JsonResponse({'success': True, 'id': cat.id, 'nombre': cat.nombre})

@grupo_requerido('Encargado', 'Gerente', 'Cajero')
def get_stock(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
        imagen_url = producto.imagen.url if producto.imagen else None
        data = {
            'stock': producto.stock,
            'precio': float(producto.precio),
            'imagen_url': imagen_url,
        }
        return JsonResponse(data)
    except Producto.DoesNotExist:
        raise Http404("Producto no encontrado")
    
@grupo_requerido('Encargado', 'Gerente')
@require_http_methods(["GET", "POST"])
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            html = render_to_string('productos/producto_form.html', {'form': form}, request)
            return JsonResponse({'success': False, 'html': html})
    else:
        form = ProductoForm()
        html = render_to_string('productos/producto_form.html', {'form': form}, request)
        return JsonResponse({'html': html})


@grupo_requerido('Encargado', 'Gerente')
@require_http_methods(["GET", "POST"])
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            html = render_to_string('productos/producto_form.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'html': html})
    else:
        form = ProductoForm(instance=producto)
        html = render_to_string('productos/producto_form.html', {'form': form}, request=request)
        return JsonResponse({'html': html})


@grupo_requerido('Encargado', 'Gerente')
@require_http_methods(["POST"])
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    try:
        producto.delete()
        return JsonResponse({'success': True})
    except Exception:
        return JsonResponse({'success': False})

from django.contrib import admin
from .models import Producto, Categoria
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

@admin.register(Producto)
class ProductoAdmin(SimpleHistoryAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'stock', 'actualizado']
    search_fields = ['nombre', 'categoria__nombre']

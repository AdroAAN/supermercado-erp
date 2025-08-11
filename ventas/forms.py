from django import forms
from .models import Venta, DetalleVenta
from productos.models import Producto
from django.forms import inlineformset_factory

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['metodo_pago']
        widgets = {
            'metodo_pago': forms.Select(attrs={
                'class': 'bg-gray-800 text-white border border-gray-600 rounded w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-lime-400'
            }),
        }

class DetalleVentaModelForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['id', 'producto', 'cantidad']
        widgets = {
            'id': forms.HiddenInput(),
            'producto': forms.Select(attrs={
                'class': 'bg-gray-800 text-white border border-gray-600 rounded w-full px-2 py-1 focus:outline-none focus:ring-2 focus:ring-lime-400 producto-select'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'bg-gray-800 text-white border border-gray-600 rounded w-full px-2 py-1 text-right focus:outline-none focus:ring-2 focus:ring-lime-400 cantidad-input',
                'min': 1
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        cantidad = cleaned_data.get('cantidad')
        if producto and cantidad:
            # Si el detalle ya existe, considera la cantidad original
            cantidad_original = 0
            if self.instance and self.instance.pk:
                cantidad_original = self.instance.cantidad
            stock_disponible = producto.stock + cantidad_original
            if stock_disponible < cantidad:
                raise forms.ValidationError(
                    f"No hay stock suficiente para {producto.nombre}. Stock disponible: {stock_disponible}."
                )
        return cleaned_data

DetalleVentaFormSet = inlineformset_factory(
    Venta,
    DetalleVenta,
    form=DetalleVentaModelForm,
    fields=('id', 'producto', 'cantidad'),
    extra=1,
    can_delete=True
)
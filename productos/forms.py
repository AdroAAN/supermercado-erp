from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'descripcion', 'imagen', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full bg-gray-700 border border-gray-600 rounded p-2 text-white focus:ring-2 focus:ring-green-500 focus:border-transparent'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'w-full bg-gray-700 border border-gray-600 rounded p-2 text-white focus:ring-2 focus:ring-green-500 focus:border-transparent'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'w-full bg-gray-700 border border-gray-600 rounded p-2 text-white focus:ring-2 focus:ring-green-500 focus:border-transparent'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full bg-gray-700 border border-gray-600 rounded p-2 text-white focus:ring-2 focus:ring-green-500 focus:border-transparent',
                'rows': 3
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'w-full bg-gray-700 border border-gray-600 rounded p-2 text-white file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-green-600 file:text-white hover:file:bg-green-500'
            }),
            'categoria': forms.Select(attrs={
                'class': 'w-full bg-gray-700 border border-gray-600 rounded p-2 text-white focus:ring-2 focus:ring-green-500 focus:border-transparent'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Asegurar que todos los campos tengan la clase base
        for field in self.fields.values():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'w-full bg-gray-700 border border-gray-600 rounded p-2 text-white focus:ring-2 focus:ring-green-500 focus:border-transparent'
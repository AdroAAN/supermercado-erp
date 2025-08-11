from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

TAILWIND_INPUT_CLASSES = (
    "bg-[#2f2f2f] border border-gray-600 rounded-md px-3 py-2 text-white "
    "focus:outline-none focus:ring-2 focus:ring-lime-400 focus:border-lime-400 w-full"
)

TAILWIND_SELECT_CLASSES = (
    "bg-[#2f2f2f] border border-gray-600 rounded-md px-3 py-2 text-white "
    "focus:outline-none focus:ring-2 focus:ring-lime-400 focus:border-lime-400 w-full"
)

TAILWIND_CHECKBOX_CLASSES = (
    "form-checkbox h-5 w-5 text-lime-500 bg-[#2f2f2f] border-gray-600 rounded"
)

class CrearUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": TAILWIND_INPUT_CLASSES})
    )
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=False,
        empty_label="Seleccione un rol",
        label="Rol",
        widget=forms.Select(attrs={"class": TAILWIND_SELECT_CLASSES})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'grupo')
        widgets = {
            "username": forms.TextInput(attrs={"class": TAILWIND_INPUT_CLASSES}),
            "password1": forms.PasswordInput(attrs={"class": TAILWIND_INPUT_CLASSES}),
            "password2": forms.PasswordInput(attrs={"class": TAILWIND_INPUT_CLASSES}),
            "is_staff": forms.CheckboxInput(attrs={"class": TAILWIND_CHECKBOX_CLASSES}),
            "is_active": forms.CheckboxInput(attrs={"class": TAILWIND_CHECKBOX_CLASSES}),
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        grupo = self.cleaned_data.get('grupo')
        if grupo:
            user.groups.add(grupo)
        return user

class EditarUsuarioForm(forms.ModelForm):
    nueva_contraseña = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={"class": TAILWIND_INPUT_CLASSES}),
        label="Nueva contraseña",
        help_text="Deja en blanco para no cambiar la contraseña."
    )
    confirmar_contraseña = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={"class": TAILWIND_INPUT_CLASSES}),
        label="Confirmar nueva contraseña"
    )
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=False,
        empty_label="Seleccione un rol",
        label="Rol",
        widget=forms.Select(attrs={"class": TAILWIND_SELECT_CLASSES})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'is_active', 'grupo')
        widgets = {
            "username": forms.TextInput(attrs={"class": TAILWIND_INPUT_CLASSES}),
            "email": forms.EmailInput(attrs={"class": TAILWIND_INPUT_CLASSES}),
            "is_staff": forms.CheckboxInput(attrs={"class": TAILWIND_CHECKBOX_CLASSES}),
            "is_active": forms.CheckboxInput(attrs={"class": TAILWIND_CHECKBOX_CLASSES}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Preseleccionar grupo actual si existe
        if self.instance:
            grupos = self.instance.groups.all()
            self.fields['grupo'].initial = grupos[0] if grupos.exists() else None

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get("nueva_contraseña")
        pwd2 = cleaned_data.get("confirmar_contraseña")

        if pwd1 or pwd2:
            if pwd1 != pwd2:
                self.add_error("confirmar_contraseña", "Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        grupo = self.cleaned_data.get('grupo')

        # Cambiar contraseña si se especificó una nueva válida
        nueva_pwd = self.cleaned_data.get('nueva_contraseña')
        if nueva_pwd:
            user.set_password(nueva_pwd)

        if commit:
            user.save()
            user.groups.clear()
            if grupo:
                user.groups.add(grupo)

        return user

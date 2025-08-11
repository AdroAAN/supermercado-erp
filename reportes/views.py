from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages

# Validador genérico para grupos permitidos
def grupos_permitidos(*nombres_grupos):
    def check(user):
        if user.is_authenticated and user.groups.filter(name__in=nombres_grupos).exists():
            return True
        # En lugar de PermissionDenied, se puede redirigir con mensaje
        return False  # esto redirige al login_url
    return check

@login_required
def dashboard(request):
    return render(request, 'reportes/dashboard.html')

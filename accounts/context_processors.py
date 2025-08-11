def permisos_y_grupos(request):
    if request.user.is_authenticated:
        grupos = list(request.user.groups.values_list('name', flat=True))
        tiene_permiso = bool(grupos) or request.user.is_superuser
    else:
        grupos = []
        tiene_permiso = False

    return {
        'user_tiene_permiso': tiene_permiso,
        'grupos_usuario': grupos,
    }
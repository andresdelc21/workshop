def nombre_sitio(request):
    return {
        'nombre_sitio': 'Mi sitio Django',
    }



def grupo_usuario(request):
    grupo = None

    if request.user.is_authenticated:
        grupos = request.user.groups.all()

        if grupos:
            grupo = grupos[0].name

    return {
        'grupo_usuario': grupo,
    }

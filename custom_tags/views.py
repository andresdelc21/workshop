from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import BusquedaUsuarioForm


@permission_required('auth.view_user', raise_exception=True)
def lista_usuarios(request):
    form = BusquedaUsuarioForm(request.GET)
    query = ''
    usuarios = User.objects.all().order_by('username')

    if form.is_valid():
        query = form.cleaned_data.get('q', '').strip()

        if query:
            usuarios = usuarios.filter(
                Q(username__icontains=query) |
                Q(email__icontains=query)
            )

    return render(request, 'custom_tags/lista_usuarios.html', {
        'form': form,
        'usuarios': usuarios,
        'query': query,
    })


class BuscarUsuariosView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'custom_tags/buscar_usuarios.html'
    permission_required = 'auth.view_user'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nombre = self.request.GET.get('nombre', '').strip()
        usuarios = User.objects.none()

        if nombre:
            usuarios = User.objects.filter(username__icontains=nombre).order_by('username')

        context['nombre'] = nombre
        context['usuarios'] = usuarios
        return context

from django.urls import path
from .views import (
    RegistroView,
    PerfilView,
    HomeView,
    AboutView,
    ContactoView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    products
)

app_name = 'core'

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('products/', products, name='products'),
    path('', PostListView.as_view(), name='post_list'),
    path('posts/', PostListView.as_view(), name='post_list_alias'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/nuevo/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/editar/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_delete'),
]
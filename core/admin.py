import logging

from django.contrib import admin, messages
from django.core.exceptions import PermissionDenied
from .forms import LibroInlineForm
from .models import Author, Libro, Tag, Post, MenuItem, SummaryCard, Product


logger = logging.getLogger(__name__)


class LibroInline(admin.TabularInline):
    model = Libro
    form = LibroInlineForm
    extra = 1
    fields = ['titulo', 'fecha_publicacion', 'descripcion']


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


class SummaryCardInline(admin.TabularInline):
    model = SummaryCard
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']
    inlines = [LibroInline, PostInline]
    change_form_template = 'admin/core/author/change_form.html'

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha_publicacion']
    list_filter = ['autor', 'fecha_publicacion']
    search_fields = ['titulo', 'autor__name']
    list_select_related = ['autor']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date']
    search_fields = ['title', 'content']
    list_filter = ['author', 'tags', 'published_date']


@admin.action(description='Activar items seleccionados')
def activar_menu_items(modeladmin, request, queryset):
    queryset.update(active=True)


@admin.action(description='Desactivar items seleccionados')
def desactivar_menu_items(modeladmin, request, queryset):
    queryset.update(active=False)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'active', 'order', 'updated_at']
    list_filter = ['active']
    search_fields = ['name', 'url']
    list_editable = ['active', 'order']
    ordering = ['order', 'name']
    readonly_fields = ['created_at', 'updated_at']
    actions = [activar_menu_items, desactivar_menu_items]
    inlines = [SummaryCardInline]



@admin.register(SummaryCard)
class SummaryCardAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'active', 'order', 'menu_item', 'updated_at']
    list_filter = ['active', 'menu_item']
    search_fields = ['title', 'description', 'url']
    list_editable = ['active', 'order']
    ordering = ['order', 'title']
    readonly_fields = ['created_at', 'updated_at']



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'active', 'created_at']
    list_filter = ['category', 'available', 'active']
    search_fields = ['name', 'category', 'description']
    list_editable = ['price', 'available', 'active']
    ordering = ['name']
    readonly_fields = ['created_at']
    actions = ['activar_productos']

    def get_queryset(self, request):
        return super().get_queryset(request).only(
            'id',
            'name',
            'category',
            'price',
            'available',
            'active',
            'created_at',
        )

    @admin.action(description='Activar productos seleccionados')
    def activar_productos(self, request, queryset):
        if not request.user.has_perm('core.change_product'):
            raise PermissionDenied('No tienes permiso para modificar productos.')

        productos_activos = queryset.filter(active=True)
        if productos_activos.exists():
            self.message_user(
                request,
                'Algunos productos seleccionados ya estaban activos.',
                messages.WARNING,
            )

        productos_inactivos = queryset.filter(active=False)
        updated = productos_inactivos.update(active=True)

        logger.info(
            'Usuario %s activo %s productos.',
            request.user,
            updated,
        )
        self.message_user(
            request,
            f'{updated} productos marcados como activos.',
            messages.SUCCESS,
        )

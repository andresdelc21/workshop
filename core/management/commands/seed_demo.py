from decimal import Decimal

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from core.models import Author, Libro, MenuItem, Product, SummaryCard


class Command(BaseCommand):
    help = 'Carga datos de ejemplo para probar el proyecto final.'

    def handle(self, *args, **options):
        menu_items = [
            ('Inicio', '/home/', 1),
            ('Productos', '/products/', 2),
            ('Publicaciones', '/', 3),
            ('Contacto', '/contacto/', 4),
            ('Admin Django', '/admin/', 5),
        ]
        for name, url, order in menu_items:
            MenuItem.objects.update_or_create(
                name=name,
                defaults={'url': url, 'order': order, 'active': True},
            )

        products = [
            ('Zapatillas urbanas', 'Calzado', Decimal('89999.99')),
            ('Remera deportiva', 'Indumentaria', Decimal('24999.50')),
            ('Mochila escolar', 'Accesorios', Decimal('35999.00')),
        ]
        for name, category, price in products:
            Product.objects.update_or_create(
                name=name,
                defaults={
                    'category': category,
                    'price': price,
                    'description': 'Producto de ejemplo para pruebas.',
                    'active': True,
                    'available': True,
                },
            )

        for title, description, url, order in [
            ('Publicaciones', 'Consulta el CRUD de posts.', '/', 1),
            ('Contacto', 'Prueba el formulario validado.', '/contacto/', 2),
            ('Productos', 'Busca productos por nombre o categoria.', '/products/', 3),
        ]:
            SummaryCard.objects.update_or_create(
                title=title,
                defaults={
                    'description': description,
                    'url': url,
                    'order': order,
                    'active': True,
                },
            )

        author, _ = Author.objects.get_or_create(
            email='autor@example.com',
            defaults={'name': 'Autor Django'},
        )
        Libro.objects.update_or_create(
            autor=author,
            titulo='Django para principiantes',
            defaults={
                'fecha_publicacion': '2024-06-01',
                'descripcion': 'Libro de ejemplo para inlines del admin.',
            },
        )

        moderadores, _ = Group.objects.get_or_create(name='Moderadores')
        editores, _ = Group.objects.get_or_create(name='Editores')
        moderadores.permissions.add(
            Permission.objects.get(codename='view_user', content_type__app_label='auth')
        )
        editores.permissions.add(*Permission.objects.filter(
            content_type__app_label='core',
            codename__in=['view_post', 'add_post', 'change_post'],
        ))

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo cargados correctamente.'))

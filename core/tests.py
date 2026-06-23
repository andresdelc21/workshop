from decimal import Decimal

from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.urls import reverse

from .forms import ContactoForm, ProductForm
from .models import Product


class ContactoFormTests(TestCase):
    def test_rechaza_email_fuera_de_example(self):
        form = ContactoForm(data={'email': 'persona@test.com'})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_acepta_email_example(self):
        form = ContactoForm(data={'email': 'persona@example.com'})
        self.assertTrue(form.is_valid())


class ProductFormTests(TestCase):
    def test_product_form_valido(self):
        form = ProductForm(data={
            'name': 'Producto Django',
            'category': 'Cursos',
            'price': '100.00',
            'description': 'Producto de prueba',
            'available': True,
        })
        self.assertTrue(form.is_valid())


class ProductSearchViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name='Remera deportiva',
            category='Indumentaria',
            price=Decimal('25000.00'),
            description='Prenda liviana',
            active=True,
            available=True,
        )
        Product.objects.create(
            name='Zapatillas urbanas',
            category='Calzado',
            price=Decimal('90000.00'),
            description='Calzado diario',
            active=True,
            available=True,
        )

    def test_filtra_por_nombre_con_get(self):
        response = self.client.get(reverse('core:products'), {'q': 'Remera'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Remera deportiva')
        self.assertNotContains(response, 'Zapatillas urbanas')

    def test_filtra_por_categoria_con_get(self):
        response = self.client.get(reverse('core:products'), {'category': 'Calzado'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Zapatillas urbanas')
        self.assertNotContains(response, 'Remera deportiva')


class UserPermissionViewTests(TestCase):
    def test_lista_usuarios_requiere_permiso(self):
        response = self.client.get(reverse('custom_tags:lista_usuarios'))
        self.assertEqual(response.status_code, 403)

    def test_usuario_con_permiso_puede_ver_lista(self):
        user = User.objects.create_user(username='moderador', password='test123')
        permission = Permission.objects.get(codename='view_user', content_type__app_label='auth')
        user.user_permissions.add(permission)
        self.client.force_login(user)

        response = self.client.get(reverse('custom_tags:lista_usuarios'), {'q': 'moderador'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'MODERADOR')

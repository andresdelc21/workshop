from django.core.exceptions import ValidationError
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    email = models.EmailField(unique=True, verbose_name='Correo electronico')

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name

class Libro(models.Model):
    autor = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='libros',
        verbose_name='Autor',
    )
    titulo = models.CharField(max_length=150, verbose_name='Titulo')
    fecha_publicacion = models.DateField(verbose_name='Fecha de publicacion')
    descripcion = models.TextField(blank=True, verbose_name='Descripcion')

    class Meta:
        ordering = ['-fecha_publicacion', 'titulo']
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published_date = models.DateTimeField(verbose_name='Fecha de publicacion')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Autor', related_name='posts')
    tags = models.ManyToManyField(Tag, verbose_name='Etiquetas', related_name='posts')

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.title

    def clean(self):
        if len(self.title) < 5:
            raise ValidationError('El titulo debe tener al menos 5 caracteres')


class MenuItem(models.Model):
    name = models.CharField(max_length=80, verbose_name='Nombre')
    url = models.CharField(max_length=200, verbose_name='URL')
    active = models.BooleanField(default=True, verbose_name='Activo')
    order = models.PositiveIntegerField(default=0, verbose_name='Orden')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Item de menu'
        verbose_name_plural = 'Items de menu'

    def __str__(self):
        return self.name



class SummaryCard(models.Model):
    title = models.CharField(max_length=120, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    url = models.CharField(max_length=200, verbose_name='URL')
    active = models.BooleanField(default=True, verbose_name='Activa')
    order = models.PositiveIntegerField(default=0, verbose_name='Orden')
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='summary_cards',
        verbose_name='Item de menu relacionado',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creada')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizada')

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Tarjeta resumen'
        verbose_name_plural = 'Tarjetas resumen'

    def __str__(self):
        return self.title

    def clean(self):
        if not self.url.startswith('/'):
            raise ValidationError('La URL debe comenzar con /.')



class Product(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nombre')
    category = models.CharField(max_length=50, default='General', verbose_name='Categoria')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Precio')
    description = models.TextField(verbose_name='Descripcion')
    active = models.BooleanField(default=True, verbose_name='Activo')
    available = models.BooleanField(default=True, verbose_name='Disponible')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')

    class Meta:
        ordering = ['name']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

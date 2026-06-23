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
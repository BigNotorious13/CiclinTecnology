from django.db import models


# Create your models here.
class Equipo(models.Model):
    clv = models.PositiveIntegerField(primary_key=True, auto_created=True, blank=False, null=False)
    nombre = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

    # Agregar funcionalidad a la clase creada
    class Meta:
        verbose_name_plural = "Equipos"


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    requisitos = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    # Agregar funcionalidad a la clase creada
    class Meta:
        verbose_name_plural = "Categorias"


class Carrera(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateTimeField()
    vueltas = models.IntegerField()
    ubicacion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    # Agregar funcionalidad a la clase creada
    class Meta:
        verbose_name_plural = "Carreras"


class Competidor(models.Model):
    id_categoria = models.IntegerField()
    id_equipo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13)
    ciudad = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    curp = models.CharField(max_length=18)
    edad = models.IntegerField()
    tipo_sangre = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre

    # Agregar funcionalidad a la clase creada
    class Meta:
        verbose_name_plural = "Competidores"

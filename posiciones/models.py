from django.db import models


class Equipo(models.Model):
    id_equipo = models.PositiveIntegerField(verbose_name='Clave', primary_key=True, blank=False, null=False)
    ciudad = models.CharField(verbose_name='Ciudad', max_length=20, null=False)
    nombre = models.CharField(verbose_name='Nombre', max_length=20, unique=True, blank=False, null=False)
    cantidad_competidores = models.PositiveIntegerField(verbose_name='Cantidad de Competidores', blank=False, null=False)

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Equipos"


class Competidor(models.Model):
    tipo_sangre = {
        ("1", "A+"),
        ("2", "A-"),
        ("3", "B+"),
        ("4", "B-"),
        ("5", "AB+"),
        ("6", "AB-"),
        ("7", "O+"),
        ("8", "O-")
    }
    id_competidor = models.PositiveIntegerField(verbose_name='Clave', primary_key=True, blank=False, null=False)
    nombre = models.CharField(verbose_name='Nombre', max_length=30, unique=True, blank=False, null=False)
    direccion = models.CharField(verbose_name='Direccion', max_length=40, null=False, blank=False)
    telefono = models.CharField(verbose_name='Telefono', max_length=10, blank=False, null=False)
    ciudad = models.CharField(verbose_name='Ciudad', max_length=20, null=False)
    estado = models.CharField(verbose_name='Estado', max_length=20, null=False)
    CURP = models.CharField(verbose_name='CURP', max_length=20, null=False)
    edad = models.PositiveIntegerField(verbose_name='Edad', blank=False, null=False)
    tipo = models.TextField(verbose_name='Tipo de Sangre', choices=tipo_sangre, blank=False)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)  # foreinKey

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Competidores"


class Categoria(models.Model):
    id_categoria = models.PositiveIntegerField(verbose_name='Clave', primary_key=True, blank=False, null=False)
    nombre = models.CharField(verbose_name='Nombre', max_length=30, unique=True, blank=False, null=False)
    requisitos = models.TextField(verbose_name='Requisitos', blank=True, null=True)
    many_comp = models.ManyToManyField(Competidor)  # muchas a muchos

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorias"


class Carrera(models.Model):
    id_carrera = models.PositiveIntegerField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(max_length=30, unique=True, blank=False, null=False)
    vueltas = models.PositiveIntegerField(blank=False, null=False)
    ubicacion = models.CharField(max_length=40, null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    many_carr_comp = models.ManyToManyField(Competidor, through="CarreraCompetidor",
                                            through_fields=('id_carrera', 'id_competidor'), )  # muchas a muchos

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Carreras"


class Organizador(models.Model):
    id_organizador = models.PositiveIntegerField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(max_length=30, unique=True, blank=False, null=False)
    usuario = models.CharField(max_length=30, unique=True, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    many_carr = models.ManyToManyField(Carrera)

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Organizadores"


class CarreraCompetidor(models.Model):
    id_carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT)  # foreinKey
    id_competidor = models.ForeignKey(Competidor, on_delete=models.PROTECT)  # foreinKey
    tiempo = models.TimeField()

    def _str_(self):
        return self.id

    class Meta:
        verbose_name_plural = "Carreras Competidores"

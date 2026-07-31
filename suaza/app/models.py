from django.db import models
from django.core.validators import FileExtensionValidator

class CarruselHero(models.Model):
    titulo = models.CharField(max_length=150, blank=True)
    subtitulo = models.CharField(max_length=250, blank=True)
    imagen = models.ImageField(upload_to='carrusel/', blank=True, null=True)
    video_fondo = models.FileField(
        upload_to='carrusel_videos/', 
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm'])]
    )
    texto_boton = models.CharField(max_length=50, blank=True, default="Saber más")
    enlace_boton = models.URLField(blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden']
        verbose_name = "Slide Carrusel"
        verbose_name_plural = "Slides Carrusel"

    def __str__(self):
        return self.titulo if self.titulo else f"Slide {self.id}"

class TarjetaInformativa(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='tarjetas/')
    enlace = models.URLField(blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)
    activa = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden', '-id']

    def __str__(self):
        return self.titulo

class SeccionDoble(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=250, blank=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='secciones_dobles/')
    alineacion_imagen_derecha = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)
    activa = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.titulo

class CampusSeccion(models.Model):
    titulo = models.CharField(max_length=150, default="Nuestro Campus")
    descripcion = models.TextField()
    imagen_fondo = models.ImageField(upload_to='campus/')
    enlace_video = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class GaleriaItem(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='galeria/')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden', '-id']

    def __str__(self):
        return self.titulo

class NoticiaEvento(models.Model):
    TIPO_CHOICES = [('NOTICIA', 'Noticia'), ('EVENTO', 'Evento')]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='NOTICIA')
    titulo = models.CharField(max_length=200)
    resumen = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='noticias/')
    fecha = models.DateField()
    activa = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"[{self.tipo}] {self.titulo}"

class SolicitudAdmision(models.Model):
    nombre_aspirante = models.CharField(max_length=150)
    apellido_aspirante = models.CharField(max_length=150)
    grado_postulacion = models.CharField(max_length=50)
    nombre_acudiente = models.CharField(max_length=150)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField(blank=True)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_envio']

    def __str__(self):
        return f"{self.nombre_aspirante} - {self.grado_postulacion}"
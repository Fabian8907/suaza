from django import forms
from .models import CarruselHero, TarjetaInformativa, SeccionDoble, CampusSeccion, GaleriaItem, NoticiaEvento, SolicitudAdmision

class CarruselForm(forms.ModelForm):
    class Meta:
        model = CarruselHero
        fields = ['titulo', 'subtitulo', 'imagen', 'video_fondo', 'texto_boton', 'enlace_boton', 'orden', 'activo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
            'subtitulo': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
            'imagen': forms.FileInput(attrs={'class': 'w-full p-2 border rounded-lg bg-gray-50'}),
            'video_fondo': forms.FileInput(attrs={'class': 'w-full p-2 border rounded-lg bg-gray-50'}),
            'texto_boton': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
            'enlace_boton': forms.URLInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
            'orden': forms.NumberInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
        }

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = TarjetaInformativa
        fields = ['titulo', 'descripcion', 'imagen', 'enlace', 'orden', 'activa']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-full p-3 border rounded-lg', 'rows': 3}),
            'imagen': forms.FileInput(attrs={'class': 'w-full p-2 border rounded-lg bg-gray-50'}),
            'enlace': forms.URLInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
            'orden': forms.NumberInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
        }

class SeccionDobleForm(forms.ModelForm):
    class Meta:
        model = SeccionDoble
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'alineacion_imagen_derecha', 'orden', 'activa']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
            'subtitulo': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
            'contenido': forms.Textarea(attrs={'class': 'w-full p-3 border rounded-lg', 'rows': 4}),
            'imagen': forms.FileInput(attrs={'class': 'w-full p-2 border rounded-lg bg-gray-50'}),
            'orden': forms.NumberInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
        }

class CampusForm(forms.ModelForm):
    class Meta:
        model = CampusSeccion
        fields = ['titulo', 'descripcion', 'imagen_fondo', 'enlace_video']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-full p-3 border rounded-lg', 'rows': 4}),
            'imagen_fondo': forms.FileInput(attrs={'class': 'w-full p-2 border rounded-lg bg-gray-50'}),
            'enlace_video': forms.URLInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
        }

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = GaleriaItem
        fields = ['titulo', 'descripcion', 'imagen', 'orden']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-full p-3 border rounded-lg', 'rows': 3}),
            'imagen': forms.FileInput(attrs={'class': 'w-full p-2 border rounded-lg bg-gray-50'}),
            'orden': forms.NumberInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
        }

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = NoticiaEvento
        fields = ['tipo', 'titulo', 'resumen', 'imagen', 'fecha', 'activa']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'w-full p-3 border rounded-lg'}),
            'titulo': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg'}),
            'resumen': forms.Textarea(attrs={'class': 'w-full p-3 border rounded-lg', 'rows': 3}),
            'imagen': forms.FileInput(attrs={'class': 'w-full p-2 border rounded-lg bg-gray-50'}),
            'fecha': forms.DateInput(attrs={'class': 'w-full p-3 border rounded-lg', 'type': 'date'}),
        }

class SolicitudAdmisionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdmision
        fields = ['nombre_aspirante', 'apellido_aspirante', 'grado_postulacion', 'nombre_acudiente', 'correo', 'telefono', 'mensaje']
        widgets = {
            'nombre_aspirante': forms.TextInput(attrs={'class': 'w-full p-4 border rounded-xl bg-gray-50 focus:ring-[#002878]'}),
            'apellido_aspirante': forms.TextInput(attrs={'class': 'w-full p-4 border rounded-xl bg-gray-50 focus:ring-[#002878]'}),
            'grado_postulacion': forms.TextInput(attrs={'class': 'w-full p-4 border rounded-xl bg-gray-50 focus:ring-[#002878]'}),
            'nombre_acudiente': forms.TextInput(attrs={'class': 'w-full p-4 border rounded-xl bg-gray-50 focus:ring-[#002878]'}),
            'correo': forms.EmailInput(attrs={'class': 'w-full p-4 border rounded-xl bg-gray-50 focus:ring-[#002878]'}),
            'telefono': forms.TextInput(attrs={'class': 'w-full p-4 border rounded-xl bg-gray-50 focus:ring-[#002878]'}),
            'mensaje': forms.Textarea(attrs={'class': 'w-full p-4 border rounded-xl bg-gray-50 focus:ring-[#002878]', 'rows': 3}),
        }
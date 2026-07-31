import os
import json
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from dotenv import load_dotenv

# NUEVO IMPORT de la librería actualizada
from google import genai 

# Importaciones de tus modelos y formularios
from .models import CarruselHero, TarjetaInformativa, SeccionDoble, CampusSeccion, GaleriaItem, NoticiaEvento, SolicitudAdmision
from .forms import CarruselForm, TarjetaForm, SeccionDobleForm, CampusForm, GaleriaForm, NoticiaForm, SolicitudAdmisionForm

# Cargar variables de entorno (tu API key)
load_dotenv()

# Configurar el cliente de la nueva API de Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    # La nueva forma de inicializar la conexión
    client = genai.Client(api_key=GEMINI_API_KEY)
else:
    client = None

def inicio(request):
    slides = CarruselHero.objects.filter(activo=True)
    tarjetas = TarjetaInformativa.objects.filter(activa=True)
    secciones_dobles = SeccionDoble.objects.filter(activa=True)
    campus = CampusSeccion.objects.first()
    galeria = GaleriaItem.objects.all()
    noticias = NoticiaEvento.objects.filter(activa=True)[:4]

    if request.method == 'POST':
        form_admision = SolicitudAdmisionForm(request.POST)
        if form_admision.is_valid():
            form_admision.save()
            messages.success(request, 'Solicitud enviada correctamente. Pronto te contactaremos.')
            return redirect('inicio')
    else:
        form_admision = SolicitudAdmisionForm()

    return render(request, 'portal/index.html', {
        'slides': slides,
        'tarjetas': tarjetas,
        'secciones_dobles': secciones_dobles,
        'campus': campus,
        'galeria': galeria,
        'noticias': noticias,
        'form_admision': form_admision
    })

# --- DASHBOARD CENTRAL ---
@login_required
def dashboard_carrusel(request):
    slides = CarruselHero.objects.all()
    if request.method == 'POST':
        form = CarruselForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_carrusel')
    else:
        form = CarruselForm()
    return render(request, 'portal/dashboard_carrusel.html', {'slides': slides, 'form': form})
@login_required
def editar_carrusel(request, pk):
    slide = get_object_or_404(CarruselHero, pk=pk)
    if request.method == 'POST':
        form = CarruselForm(request.POST, request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            return redirect('dashboard_carrusel')
    else:
        form = CarruselForm(instance=slide)
    return render(request, 'portal/dashboard_editar.html', {'form': form, 'titulo': 'Editar Slide', 'volver': 'dashboard_carrusel'})
@login_required
def eliminar_carrusel(request, pk):
    get_object_or_404(CarruselHero, pk=pk).delete()
    return redirect('dashboard_carrusel')
@login_required
def dashboard_tarjetas(request):
    tarjetas = TarjetaInformativa.objects.all()
    if request.method == 'POST':
        form = TarjetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_tarjetas')
    else:
        form = TarjetaForm()
    return render(request, 'portal/dashboard_tarjetas.html', {'tarjetas': tarjetas, 'form': form})
@login_required
def editar_tarjeta(request, pk):
    tarjeta = get_object_or_404(TarjetaInformativa, pk=pk)
    if request.method == 'POST':
        form = TarjetaForm(request.POST, request.FILES, instance=tarjeta)
        if form.is_valid():
            form.save()
            return redirect('dashboard_tarjetas')
    else:
        form = TarjetaForm(instance=tarjeta)
    return render(request, 'portal/dashboard_editar.html', {'form': form, 'titulo': 'Editar Tarjeta', 'volver': 'dashboard_tarjetas'})
@login_required
def eliminar_tarjeta(request, pk):
    get_object_or_404(TarjetaInformativa, pk=pk).delete()
    return redirect('dashboard_tarjetas')
@login_required
def dashboard_secciones(request):
    secciones = SeccionDoble.objects.all()
    if request.method == 'POST':
        form = SeccionDobleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_secciones')
    else:
        form = SeccionDobleForm()
    return render(request, 'portal/dashboard_secciones.html', {'secciones': secciones, 'form': form})
@login_required
def editar_seccion(request, pk):
    seccion = get_object_or_404(SeccionDoble, pk=pk)
    if request.method == 'POST':
        form = SeccionDobleForm(request.POST, request.FILES, instance=seccion)
        if form.is_valid():
            form.save()
            return redirect('dashboard_secciones')
    else:
        form = SeccionDobleForm(instance=seccion)
    return render(request, 'portal/dashboard_editar.html', {'form': form, 'titulo': 'Editar Sección Doble', 'volver': 'dashboard_secciones'})
@login_required
def eliminar_seccion(request, pk):
    get_object_or_404(SeccionDoble, pk=pk).delete()
    return redirect('dashboard_secciones')
@login_required
def dashboard_campus(request):
    campus, _ = CampusSeccion.objects.get_or_create(id=1, defaults={'titulo': 'Nuestro Campus', 'descripcion': 'Edita esto'})
    if request.method == 'POST':
        form = CampusForm(request.POST, request.FILES, instance=campus)
        if form.is_valid():
            form.save()
            return redirect('dashboard_campus')
    else:
        form = CampusForm(instance=campus)
    return render(request, 'portal/dashboard_campus.html', {'form': form, 'campus': campus})
@login_required
def dashboard_galeria(request):
    items = GaleriaItem.objects.all()
    if request.method == 'POST':
        form = GaleriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_galeria')
    else:
        form = GaleriaForm()
    return render(request, 'portal/dashboard_galeria.html', {'items': items, 'form': form})
@login_required
def eliminar_galeria(request, pk):
    get_object_or_404(GaleriaItem, pk=pk).delete()
    return redirect('dashboard_galeria')
@login_required
def dashboard_noticias(request):
    noticias = NoticiaEvento.objects.all()
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_noticias')
    else:
        form = NoticiaForm()
    return render(request, 'portal/dashboard_noticias.html', {'noticias': noticias, 'form': form})
@login_required
def eliminar_noticia(request, pk):
    get_object_or_404(NoticiaEvento, pk=pk).delete()
    return redirect('dashboard_noticias')
@login_required
def dashboard_admisiones(request):
    solicitudes = SolicitudAdmision.objects.all()
    return render(request, 'portal/dashboard_admisiones.html', {'solicitudes': solicitudes})

# --- VISTA PARA TYQUY BOT (INTELIGENCIA ARTIFICIAL) ---

def api_chat_bot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('prompt', '')
            
            # Obtener la llave desde el .env
            OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
            
            if not OPENROUTER_API_KEY:
                return JsonResponse({'reply': 'La API Key de OpenRouter no está configurada en el servidor.'})

            contexto_bot = (
                "Eres Tyquy, el asistente virtual oficial de la Institución Educativa Suazapawa, "
                "ubicada en Sogamoso, Boyacá. Responde siempre de forma amable, corta (máximo 3 párrafos cortos) "
                "y útil. Si no sabes algo, invita al usuario a usar la sección 'Contáctenos' o el botón de WhatsApp. "
            )
            
            # Preparar el paquete de datos para OpenRouter
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            }
            
            payload = {
                # openrouter/free elige automáticamente el mejor modelo gratuito disponible (puede incluir Llama o variaciones de DeepSeek gratuitas)
                # Si algún día pagas créditos en OpenRouter, solo cambias esto por 'deepseek/deepseek-chat'
                "model": "openrouter/free", 
                "messages": [
                    {"role": "system", "content": contexto_bot},
                    {"role": "user", "content": user_message}
                ]
            }
            
            # Llamar a la API
            respuesta_api = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload
            )
            
            datos_respuesta = respuesta_api.json()
            
            # Extraer el texto de la respuesta
            bot_reply = datos_respuesta['choices'][0]['message']['content'].replace('\n', '<br>')
            
            return JsonResponse({'reply': bot_reply})
            
        except Exception as e:
            print(f"Error en IA: {e}")
            return JsonResponse({'reply': 'Lo siento, tuve un pequeño fallo en mis circuitos. ¿Podrías intentar preguntar de nuevo?'})
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def transporte(request):
    return render(request, 'portal/transporte.html')

def restaurante(request):
    return render(request, 'portal/restaurante.html')

def enfermeria(request):
    return render(request, 'portal/enfermeria.html')

def seguridad(request):
    return render(request, 'seguridad.html')
def alumno(request):
    return render(request, 'portal/alumno.html')

def docente(request):
    return render(request, 'portal/docente.html')

def misionvision(request):
    return render(request, 'portal/misionvision.html')

def somos(request):
    return render(request, 'portal/somos.html')
def ubicacion(request):
    return render(request, 'portal/ubicacion.html')



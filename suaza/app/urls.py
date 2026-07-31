from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # --- SISTEMA DE LOGIN ---
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    
    # --- DASHBOARD PROTEGIDO ---
    path('dashboard/carrusel/', views.dashboard_carrusel, name='dashboard_carrusel'),
    path('dashboard/carrusel/editar/<int:pk>/', views.editar_carrusel, name='editar_carrusel'),
    path('dashboard/carrusel/eliminar/<int:pk>/', views.eliminar_carrusel, name='eliminar_carrusel'),
    path('dashboard/tarjetas/', views.dashboard_tarjetas, name='dashboard_tarjetas'),
    path('dashboard/tarjetas/editar/<int:pk>/', views.editar_tarjeta, name='editar_tarjeta'),
    path('dashboard/tarjetas/eliminar/<int:pk>/', views.eliminar_tarjeta, name='eliminar_tarjeta'),
    path('dashboard/secciones/', views.dashboard_secciones, name='dashboard_secciones'),
    path('dashboard/secciones/editar/<int:pk>/', views.editar_seccion, name='editar_seccion'),
    path('dashboard/secciones/eliminar/<int:pk>/', views.eliminar_seccion, name='eliminar_seccion'),
    path('dashboard/campus/', views.dashboard_campus, name='dashboard_campus'),
    path('dashboard/galeria/', views.dashboard_galeria, name='dashboard_galeria'),
    path('dashboard/galeria/eliminar/<int:pk>/', views.eliminar_galeria, name='eliminar_galeria'),
    path('dashboard/noticias/', views.dashboard_noticias, name='dashboard_noticias'),
    path('dashboard/noticias/eliminar/<int:pk>/', views.eliminar_noticia, name='eliminar_noticia'),
    path('dashboard/admisiones/', views.dashboard_admisiones, name='dashboard_admisiones'),
    
    # --- RUTAS PÚBLICAS ---
    path('api/chat/', views.api_chat_bot, name='api_chat_bot'),
    path('transporte/', views.transporte, name='transporte'),
    path('restaurante/', views.restaurante, name='restaurante'),
    path('enfermeria/', views.enfermeria, name='enfermeria'),
    path('seguridad/', views.seguridad, name='seguridad'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('somos/', views.somos, name='somos'),
    path('misionvision/', views.misionvision, name='misionvision'),
    path('docente/', views.docente, name='docente'),
    path('alumno/', views.alumno, name='alumno'),
]
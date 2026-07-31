import os
import sys

# Añade la ruta física del proyecto al sistema
sys.path.insert(0, os.path.dirname(__file__))

# Indica qué archivo de configuración se debe usar
# IMPORTANTE: Reemplaza 'nombre_de_tu_proyecto' por el nombre exacto de 
# la carpeta que contiene tu archivo settings.py y wsgi.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'nombre_de_tu_proyecto.settings'

# Levanta la aplicación WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
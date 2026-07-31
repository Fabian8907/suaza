from django.contrib import admin
from .models import TarjetaInformativa

@admin.register(TarjetaInformativa)
class TarjetaInformativaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'activa')
    list_editable = ('orden', 'activa')
    search_fields = ('titulo',)
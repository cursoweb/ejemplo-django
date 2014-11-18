#!env/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from encuestas.models import Pregunta, Eleccion, Noticia
from imagekit.admin import AdminThumbnail

class EleccionInline(admin.TabularInline):
    model = Eleccion
    extra = 3    # Aqui ndicamos la cantidad de "slots" que hay de elecciones, el 
                 # usuario puede agregar más si lo necesita


class PreguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['texto_pregunta']}),
        (u'Información de fecha', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [EleccionInline]   # Le indicamos a Django que las elecciones se 
                                 # cargan desde el admin de Pregunta
    list_display = ('texto_pregunta', 'pub_date', 
                    'fue_publicada_recientemente')
    list_filter = ['pub_date']
    search_fields = ['texto_pregunta']
    date_hierarchy = 'pub_date'

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='imagen_thumbnail')


admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Eleccion)
admin.site.register(Noticia, NoticiaAdmin)

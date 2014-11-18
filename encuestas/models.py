# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha publicada')

    def __unicode__(self):              # __str__ en Python 3
        return self.texto_pregunta

    def fue_publicada_recientemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    fue_publicada_recientemente.admin_order_field = 'pub_date'
    fue_publicada_recientemente.boolean = True
    fue_publicada_recientemente.short_description = 'Publicada recientemente?'


class Eleccion(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    texto_opcion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __unicode__(self):              # __str__ en Python 3
        return self.texto_opcion

    class Meta:
        verbose_name_plural = "elecciones"


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenidos = RichTextField()

    imagen = models.ImageField(upload_to='noticias', null=True, blank=True)

    imagen_thumbnail = ImageSpecField(source='imagen',
                                      processors=[ResizeToFill(50, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    imagen_principal = ImageSpecField(source='imagen',
                                      processors=[ResizeToFit(800)],
                                      format='JPEG',
                                      options={'quality': 80})

    def __unicode__(self):              # __str__ en Python 3
        return self.titulo

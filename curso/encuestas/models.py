# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.utils import timezone

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha publicada')    

    def __unicode__(self):              # __str__ en Python 3
        return self.texto_pregunta

    def fue_publicada_recientemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Eleccion(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    texto_opcion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __unicode__(self):              # __str__ en Python 3
        return self.texto_opcion
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from encuestas.models import Eleccion, Pregunta


class IndexView(generic.ListView):
    template_name = 'encuestas/index.html'
    context_object_name = 'lista_ultimas_preguntas'

    def get_queryset(self):
        """Retorna las ultimas 5 preguntas."""
        return Pregunta.objects.order_by('-pub_date')[:5]

class ResultadosView(generic.DetailView):
    model = Pregunta
    template_name = 'encuestas/resultados.html'



def votar(request, pregunta_id):
    p = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        opcion_elegida = p.eleccion_set.get(pk=request.POST['eleccion'])
    except (KeyError, Eleccion.DoesNotExist):
        # Volver a mostrar el formulario para votar.
        return render(request, 'encuestas/detalle.html', {
            'pregunta': p,
            'error_message': u"No seleccionaste una opción.",
        })
    else:
        opcion_elegida.votos += 1
        opcion_elegida.save()
        # siempre retornar un HttpResponseRedirect después de lidiar
        # exitosamente con datos de POST. Esto evita que los datos sean
        # posteados 2 veces si el usuario presiona el botón de Atrás.
        return HttpResponseRedirect(reverse('encuestas:resultados', args=(p.id,)))
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0002_auto_20141118_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='contenido',
        ),
        migrations.AddField(
            model_name='noticia',
            name='contenidos',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

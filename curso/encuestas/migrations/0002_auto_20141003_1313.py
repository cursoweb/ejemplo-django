# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eleccion',
            old_name='text_opcion',
            new_name='texto_opcion',
        ),
    ]

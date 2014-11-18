# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0003_auto_20141118_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'noticias', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='contenidos',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

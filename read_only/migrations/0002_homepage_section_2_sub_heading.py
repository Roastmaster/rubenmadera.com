# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-20 23:28
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('read_only', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='section_2_sub_heading',
            field=mezzanine.core.fields.RichTextField(default='Just a cute site with nothing really going for it besides the design tbh', help_text='Maybe a brief description of who you are or something', max_length=1000),
            preserve_default=False,
        ),
    ]

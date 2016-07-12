# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
    ]
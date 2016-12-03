# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-03 13:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/img_usr')),
            ],
        ),
        migrations.CreateModel(
            name='Dispositivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/img_usr')),
                ('id_persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='id_persona', to=settings.AUTH_USER_MODEL)),
                ('usr2', models.ManyToManyField(related_name='_usuarios_usr2_+', to='cuentas.Usuarios')),
            ],
        ),
        migrations.AddField(
            model_name='alarma',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuentas.Dispositivos'),
        ),
    ]
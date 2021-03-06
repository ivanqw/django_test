# Generated by Django 2.1 on 2018-10-13 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('contenido', models.TextField(verbose_name='contenido')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Creación')),
                ('fecha_publicacion', models.DateField(blank=True, null=True, verbose_name='Fecha Publicación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

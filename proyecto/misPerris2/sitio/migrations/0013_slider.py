# Generated by Django 2.1 on 2018-11-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0012_auto_20181103_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='slider')),
                ('descripcion', models.TextField(verbose_name='descripcion')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]

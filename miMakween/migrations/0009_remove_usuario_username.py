# Generated by Django 4.2 on 2023-05-24 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miMakween', '0008_usuario_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
    ]

# Generated by Django 4.2 on 2023-06-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miMakween', '0012_servicio_alter_usuario_user_orden_itemorden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='precio',
            field=models.IntegerField(),
        ),
    ]

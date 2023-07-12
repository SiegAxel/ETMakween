# Generated by Django 4.2 on 2023-05-24 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miMakween', '0006_usuario_alter_trabajos_mecanico'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='trabajos',
            options={'verbose_name': 'Trabajo', 'verbose_name_plural': 'Trabajos'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to='miMakween.categoria'),
        ),
    ]

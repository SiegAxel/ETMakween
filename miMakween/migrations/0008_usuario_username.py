# Generated by Django 4.2 on 2023-05-24 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miMakween', '0007_alter_categoria_options_alter_trabajos_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=45, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-12 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atracao',
            old_name='ideade_minima',
            new_name='idade_minima',
        ),
    ]
# Generated by Django 3.1.2 on 2020-10-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_auto_20201012_1542'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
    ]
# Generated by Django 3.1.2 on 2020-10-16 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0004_atracao_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='observacoes',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]

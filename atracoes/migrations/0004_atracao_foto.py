# Generated by Django 3.1.2 on 2020-10-13 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0003_auto_20201013_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]

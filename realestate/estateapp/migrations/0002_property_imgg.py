# Generated by Django 4.0.4 on 2022-06-11 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estateapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='imgg',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]

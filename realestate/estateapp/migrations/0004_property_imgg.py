# Generated by Django 4.0.4 on 2022-06-13 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estateapp', '0003_remove_property_imgg'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='imgg',
            field=models.ImageField(default='', upload_to='imgs/'),
            preserve_default=False,
        ),
    ]

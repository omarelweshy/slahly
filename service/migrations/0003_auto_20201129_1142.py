# Generated by Django 3.1.3 on 2020-11-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image2',
            field=models.ImageField(height_field=200, upload_to='service_images', verbose_name='ii', width_field=300),
        ),
    ]

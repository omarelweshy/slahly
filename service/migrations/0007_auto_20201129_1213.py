# Generated by Django 3.1.3 on 2020-11-29 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20201129_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'الخدمة', 'verbose_name_plural': 'الخدمات'},
        ),
        migrations.RemoveField(
            model_name='service',
            name='image2',
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default=None, upload_to='service_images', verbose_name='صورة الخدمة'),
            preserve_default=False,
        ),
    ]

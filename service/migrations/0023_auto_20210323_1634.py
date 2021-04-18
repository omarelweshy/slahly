# Generated by Django 3.1.3 on 2021-03-23 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0022_employeeworkimages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeeworkimages',
            options={'verbose_name': 'صورة العمل', 'verbose_name_plural': 'صور العمل'},
        ),
        migrations.AlterField(
            model_name='employeeworkimages',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_images', to='service.employee', verbose_name='العامل'),
        ),
    ]
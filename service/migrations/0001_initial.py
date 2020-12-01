# Generated by Django 3.1.3 on 2020-12-01 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='اسم الخدمة')),
                ('image', models.ImageField(upload_to='service_images', verbose_name='صورة الخدمة')),
            ],
            options={
                'verbose_name': 'الخدمة',
                'verbose_name_plural': 'الخدمات',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='اسم الموظف')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='service.service', verbose_name='الخدمة')),
            ],
            options={
                'verbose_name': 'الموظف',
                'verbose_name_plural': 'الموظفين',
            },
        ),
    ]

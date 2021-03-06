# Generated by Django 3.1.3 on 2021-04-27 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0003_auto_20210427_1729'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.TextField(verbose_name='المشكلة')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='وقت الطلب')),
                ('status', models.BooleanField(default=False, verbose_name='تم تنفيذ الخدمة')),
                ('show_in_history', models.BooleanField(default=True, verbose_name='إظهار فى السجل')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.employee', verbose_name='الموظف')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'الطلب',
                'verbose_name_plural': 'الطلبات',
                'ordering': ['-id'],
            },
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-11 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0017_auto_20201211_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='show_in_history',
            field=models.BooleanField(default=True, verbose_name='إظهار فى السجل'),
        ),
    ]

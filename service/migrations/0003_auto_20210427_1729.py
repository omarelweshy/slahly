# Generated by Django 3.1.3 on 2021-04-27 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20210427_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spareparts',
            name='service',
        ),
        migrations.DeleteModel(
            name='Request',
        ),
        migrations.DeleteModel(
            name='SpareParts',
        ),
    ]

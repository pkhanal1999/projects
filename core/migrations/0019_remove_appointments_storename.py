# Generated by Django 2.2 on 2020-01-14 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_appointments_storename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='storename',
        ),
    ]

# Generated by Django 2.2 on 2020-01-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_appointments_storename'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='storename',
            field=models.CharField(default='STORENAME', max_length=20),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.2 on 2020-01-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_delete_appointments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storename', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('datemonth', models.CharField(max_length=2)),
                ('dateday', models.CharField(max_length=2)),
                ('dateyear', models.CharField(max_length=4)),
                ('timehour', models.CharField(max_length=2)),
                ('timemin', models.CharField(max_length=2)),
                ('ampm', models.CharField(max_length=4)),
            ],
        ),
    ]

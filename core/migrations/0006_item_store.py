# Generated by Django 2.2 on 2020-01-13 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200113_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='store',
            field=models.CharField(default='B', max_length=100),
            preserve_default=False,
        ),
    ]

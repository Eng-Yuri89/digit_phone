# Generated by Django 4.0.1 on 2022-01-12 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imei',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]

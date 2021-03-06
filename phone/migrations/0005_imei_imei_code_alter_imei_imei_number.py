# Generated by Django 4.0.1 on 2022-01-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0004_imei_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='imei',
            name='imei_code',
            field=models.CharField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imei',
            name='imei_number',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]

# Generated by Django 4.0 on 2022-01-08 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Egypt Pound', max_length=20, unique=True)),
                ('code', models.CharField(default='EGP', max_length=5, unique=True)),
                ('exchange', models.DecimalField(blank=True, decimal_places=2, default=6.99, max_digits=8, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=20, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Nigne', max_length=10)),
                ('content', models.CharField(default='', max_length=300)),
                ('slug', models.SlugField(default='nigne', max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='English', max_length=20, unique=True)),
                ('code', models.CharField(default='en', max_length=5, unique=True)),
                ('image', models.ImageField(default='images/lang/en-gb.png', null=True, upload_to='images/lang/%Y/%m/%d')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Waiting', 'Waiting for activation'), ('Inactive', 'Inactive')], max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Governorates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Qena', max_length=30)),
                ('name_ar', models.CharField(default='قنا', max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Qena', max_length=50)),
                ('name_ar', models.CharField(default='Qena', max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('governorates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.governorates')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Qena', max_length=30)),
                ('name_ar', models.CharField(default='Qena', max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city')),
            ],
        ),
    ]

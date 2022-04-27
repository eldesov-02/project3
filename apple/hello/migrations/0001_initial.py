# Generated by Django 4.0.4 on 2022-04-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postusers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250, verbose_name='Username')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('address', models.CharField(max_length=30, verbose_name='Address')),
            ],
        ),
    ]

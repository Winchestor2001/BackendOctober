# Generated by Django 4.1.5 on 2023-01-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('fee', models.FloatField(default=0)),
                ('roll_no', models.IntegerField(unique=True)),
                ('gender', models.CharField(choices=[('M', 'Erkak'), ('F', 'Ayol')], max_length=50)),
                ('address', models.TextField()),
                ('is_registered', models.BooleanField(default=False)),
            ],
        ),
    ]

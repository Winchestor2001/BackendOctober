# Generated by Django 4.1.6 on 2023-02-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_todo_complated_todo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='complated',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]

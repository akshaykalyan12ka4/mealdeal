# Generated by Django 3.2.15 on 2022-08-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mains',
            name='url',
            field=models.URLField(blank=True, default=''),
        ),
    ]

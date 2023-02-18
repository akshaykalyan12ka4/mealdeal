# Generated by Django 3.2.15 on 2022-08-23 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0006_mealplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='day_friday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_friday', to='planner.meal'),
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='day_monday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_monday', to='planner.meal'),
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='day_saturday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_saturday', to='planner.meal'),
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='day_sunday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_sunday', to='planner.meal'),
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='day_thursday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_thursday', to='planner.meal'),
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='day_tuesday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_tuesday', to='planner.meal'),
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='day_wednesday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_wednesday', to='planner.meal'),
        ),
    ]
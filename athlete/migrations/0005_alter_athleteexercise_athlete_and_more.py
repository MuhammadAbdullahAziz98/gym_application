# Generated by Django 4.1.1 on 2022-10-03 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('athlete', '0004_remove_athleteexercise_exercise_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athleteexercise',
            name='athlete',
            field=models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='athlete', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='athleteexercise',
            name='exercise',
            field=models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='exercise.exercise'),
        ),
    ]

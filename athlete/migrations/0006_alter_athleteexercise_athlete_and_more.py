# Generated by Django 4.1.1 on 2022-10-03 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercise', '0001_initial'),
        ('athlete', '0005_alter_athleteexercise_athlete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athleteexercise',
            name='athlete',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='athlete', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='athleteexercise',
            name='exercise',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='exercise.exercise'),
        ),
    ]

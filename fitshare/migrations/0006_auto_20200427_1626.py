# Generated by Django 3.0.5 on 2020-04-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitshare', '0005_workout_user_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout_e',
            name='time',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='workout_e',
            name='desc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='workout_e',
            name='reps',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='workout_e',
            name='sets',
            field=models.IntegerField(null=True),
        ),
    ]

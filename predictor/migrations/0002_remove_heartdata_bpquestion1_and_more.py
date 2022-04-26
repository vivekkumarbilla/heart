# Generated by Django 4.0.4 on 2022-04-21 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heartdata',
            name='bpquestion1',
        ),
        migrations.RemoveField(
            model_name='heartdata',
            name='bpquestion2',
        ),
        migrations.RemoveField(
            model_name='heartdata',
            name='bpquestion3',
        ),
        migrations.RemoveField(
            model_name='heartdata',
            name='bpquestion4',
        ),
        migrations.RemoveField(
            model_name='heartdata',
            name='dquestion1',
        ),
        migrations.RemoveField(
            model_name='heartdata',
            name='dquestion2',
        ),
        migrations.RemoveField(
            model_name='heartdata',
            name='dquestion3',
        ),
        migrations.RemoveField(
            model_name='heartdata',
            name='dquestion4',
        ),
        migrations.AlterField(
            model_name='heartdata',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (0, 'Female')], verbose_name='Gender'),
        ),
    ]

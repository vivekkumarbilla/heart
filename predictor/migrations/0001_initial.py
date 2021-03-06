# Generated by Django 4.0.4 on 2022-04-21 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorHospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=25)),
                ('hospital_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField()),
                ('Location', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='HeartData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('gender', models.IntegerField(choices=[('-', 'Select an Option'), (1, 'Male'), (0, 'Female')], verbose_name='Gender')),
                ('activity', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Breathlessness during activity')),
                ('rest', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Breathlessness at rest')),
                ('night', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Awake by Breathlessness at night')),
                ('exercise', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Exercise induced angina (chest pain after exercise)')),
                ('diabetes', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Diabetic')),
                ('dquestion1', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Diabetic Question 1')),
                ('dquestion2', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Diabetic Question 2')),
                ('dquestion3', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Diabetic Question 3')),
                ('dquestion4', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Diabetic Question 4')),
                ('bp', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Blood Pressure')),
                ('bpquestion1', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Blood Pressure Question 1')),
                ('bpquestion2', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Blood Pressure Question 2')),
                ('bpquestion3', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Blood Pressure Question 3')),
                ('bpquestion4', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Blood Pressure Question 4')),
                ('cyanosis', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Cyanosis')),
                ('clubbing', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Clubbing')),
                ('date', models.DateField(auto_now_add=True)),
                ('probability', models.FloatField(null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

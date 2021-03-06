# Generated by Django 2.2.4 on 2019-12-25 19:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraduateAdmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gre_score', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(260), django.core.validators.MaxValueValidator(340)])),
                ('toefl_score', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(120)])),
                ('university_rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('sop_rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('lor_rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('research', models.PositiveIntegerField(choices=[(0, 0), (1, 1)], default=0)),
                ('cgpa', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
    ]

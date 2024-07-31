# Generated by Django 4.2.3 on 2024-07-14 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BirdFluData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_collected', models.DateField()),
                ('end_date_collected', models.DateField()),
                ('region', models.CharField(default='Unknown', max_length=100)),
                ('iso_code', models.CharField(default='Unknown', max_length=10)),
                ('country_code', models.CharField(default='Unknown', max_length=10)),
                ('country', models.CharField(default='Unknown', max_length=100)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('hpai_strain', models.CharField(default='Unknown', max_length=100)),
                ('woah_classification', models.CharField(default='Unknown', max_length=100)),
                ('new_outbreaks', models.IntegerField(default=0.0)),
                ('cumulative_outbreaks', models.IntegerField(default=0.0)),
            ],
        ),
    ]

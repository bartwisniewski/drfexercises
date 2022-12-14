# Generated by Django 4.1.2 on 2022-10-24 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('mode', models.CharField(choices=[('off', 'OFF'), ('man', 'MANUAL'), ('auto', 'AUTO')], default='off', max_length=4)),
                ('on', models.BooleanField(default=False)),
                ('feedback', models.BooleanField(default=False)),
                ('max_pressure', models.FloatField(default=5.0)),
                ('nominal_flow', models.FloatField(default=10.0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Valve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('mode', models.CharField(choices=[('off', 'OFF'), ('man', 'MANUAL'), ('auto', 'AUTO')], default='off', max_length=4)),
                ('open', models.BooleanField(default=False)),
                ('feedback_open', models.BooleanField(default=False)),
                ('feedback_close', models.BooleanField(default=True)),
                ('time_monitoring', models.FloatField(default=5.0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

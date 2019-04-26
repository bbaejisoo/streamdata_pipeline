# Generated by Django 2.1.7 on 2019-04-25 10:15

import datetime
from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grafana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('embed_url', models.URLField()),
                ('start_time', models.DateTimeField(default=datetime.datetime.now)),
                ('end_time', models.DateTimeField(default=home.models.now_plus_15min)),
            ],
        ),
    ]

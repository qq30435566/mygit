# Generated by Django 2.0 on 2018-04-05 00:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20180405_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 5, 0, 7, 54, 659868, tzinfo=utc)),
        ),
    ]

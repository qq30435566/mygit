# Generated by Django 2.0 on 2018-04-04 23:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 4, 23, 53, 37, 955867, tzinfo=utc)),
        ),
    ]

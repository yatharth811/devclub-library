# Generated by Django 3.2 on 2021-04-29 11:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_bookrequest_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 17, 1, 7, 926552)),
        ),
    ]

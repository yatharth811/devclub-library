# Generated by Django 3.2 on 2021-04-29 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_bookrequest_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 15, 29, 40, 325237)),
        ),
    ]
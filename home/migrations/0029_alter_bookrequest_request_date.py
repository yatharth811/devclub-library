# Generated by Django 3.2 on 2021-04-29 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_remove_bookrequest_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 14, 36, 46, 773599)),
        ),
    ]
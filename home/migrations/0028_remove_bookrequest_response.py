# Generated by Django 3.2 on 2021-04-29 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20210429_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookrequest',
            name='response',
        ),
    ]
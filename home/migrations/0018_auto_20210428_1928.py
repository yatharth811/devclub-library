# Generated by Django 3.2 on 2021-04-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_bookissue_bookrequest_bookreturn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookrequest',
            name='response',
        ),
        migrations.AddField(
            model_name='bookissue',
            name='response',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookreturn',
            name='response',
            field=models.BooleanField(default=False),
        ),
    ]

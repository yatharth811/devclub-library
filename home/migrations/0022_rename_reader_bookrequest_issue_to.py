# Generated by Django 3.2 on 2021-04-28 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_bookrequest_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookrequest',
            old_name='reader',
            new_name='issue_to',
        ),
    ]

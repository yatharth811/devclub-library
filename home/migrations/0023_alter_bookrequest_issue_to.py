# Generated by Django 3.2 on 2021-04-28 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_rename_reader_bookrequest_issue_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrequest',
            name='issue_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
    ]

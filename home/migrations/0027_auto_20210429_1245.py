# Generated by Django 3.2 on 2021-04-29 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20210429_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrequest',
            name='status',
            field=models.CharField(choices=[('ACC', 'Accept'), ('REJ', 'Reject'), ('PEN', 'Pending')], default='PEN', help_text='Issue Status', max_length=3),
        ),
        migrations.DeleteModel(
            name='BookIssue',
        ),
    ]

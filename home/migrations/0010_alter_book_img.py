# Generated by Django 3.2 on 2021-04-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210428_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(default='default.png', upload_to='media/'),
        ),
    ]
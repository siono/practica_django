# Generated by Django 2.0.1 on 2018-01-08 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20180105_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categories',
        ),
    ]

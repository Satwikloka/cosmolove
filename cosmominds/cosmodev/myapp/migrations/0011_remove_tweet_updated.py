# Generated by Django 4.0.1 on 2022-02-18 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_tweet_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='updated',
        ),
    ]

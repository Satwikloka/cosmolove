# Generated by Django 4.0.1 on 2022-07-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_tweet_id_alter_tweet_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='id',
        ),
        migrations.AddField(
            model_name='tweet',
            name='sid',
            field=models.AutoField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
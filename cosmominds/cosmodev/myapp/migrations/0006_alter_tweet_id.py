# Generated by Django 4.0.1 on 2022-02-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_tweet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.TextField(blank=True, primary_key=True, serialize=False),
        ),
    ]
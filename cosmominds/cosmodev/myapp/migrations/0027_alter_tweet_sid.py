# Generated by Django 4.0.1 on 2022-07-29 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_tweet_sid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='sid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
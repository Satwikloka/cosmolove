# Generated by Django 4.0.1 on 2022-02-14 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.TextField(blank=True, primary_key=True, serialize=False),
        ),
    ]
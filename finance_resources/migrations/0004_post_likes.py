# Generated by Django 4.1.5 on 2023-04-30 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_resources', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.8 on 2022-04-10 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20220410_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 20, 7, 43, 771782)),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 20, 7, 43, 771782)),
        ),
    ]

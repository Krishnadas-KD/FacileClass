# Generated by Django 3.2.8 on 2022-06-30 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20220630_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 30, 22, 44, 18, 40652)),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 30, 22, 44, 18, 40652)),
        ),
    ]

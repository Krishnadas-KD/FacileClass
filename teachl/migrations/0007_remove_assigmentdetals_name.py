# Generated by Django 3.2.8 on 2022-06-05 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachl', '0006_assigmentdetals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assigmentdetals',
            name='name',
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-14 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='location',
        ),
    ]

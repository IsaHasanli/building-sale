# Generated by Django 4.1.4 on 2022-12-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='have_community_center',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_message_email_alter_message_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_visible',
            field=models.BooleanField(default=False),
        ),
    ]

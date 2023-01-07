# Generated by Django 4.1.4 on 2022-12-14 10:46

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('location', djgeojson.fields.PointField()),
                ('location_name', models.CharField(max_length=100)),
            ],
        ),
    ]
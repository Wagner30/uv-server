# Generated by Django 3.0.2 on 2020-01-29 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uvIntensity', models.CharField(blank=True, default='', max_length=10)),
                ('uvIndex', models.CharField(blank=True, default='', max_length=10)),
            ],
        ),
    ]

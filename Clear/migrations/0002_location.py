# Generated by Django 3.2.9 on 2022-12-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clear', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
    ]

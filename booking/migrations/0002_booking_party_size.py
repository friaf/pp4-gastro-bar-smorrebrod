# Generated by Django 3.2.19 on 2023-05-17 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='party_size',
            field=models.IntegerField(default=2),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatsapp',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
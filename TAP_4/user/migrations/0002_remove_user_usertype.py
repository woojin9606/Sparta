# Generated by Django 4.0.4 on 2022-06-17 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='usertype',
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-22 05:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_article_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 14, 28, 39, 783609), verbose_name='노출 시작'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 29, 14, 28, 39, 783609), verbose_name='노출 종료'),
        ),
    ]

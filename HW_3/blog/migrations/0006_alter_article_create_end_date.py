# Generated by Django 4.0.5 on 2022-06-20 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_create_end_date_alter_article_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 25, 16, 37, 8, 851036), verbose_name='노출 종료'),
        ),
    ]
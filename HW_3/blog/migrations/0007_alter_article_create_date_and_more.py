# Generated by Django 4.0.5 on 2022-06-20 07:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_create_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 16, 40, 13, 131217), verbose_name='노출 시작'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 25, 16, 40, 13, 131217), verbose_name='노출 종료'),
        ),
    ]
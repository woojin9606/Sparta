# Generated by Django 4.0.5 on 2022-06-22 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='등록일자'),
        ),
    ]

# Generated by Django 3.2.9 on 2022-06-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Price',
            field=models.IntegerField(),
        ),
    ]
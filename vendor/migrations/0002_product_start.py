# Generated by Django 3.0.5 on 2022-03-08 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='start',
            field=models.CharField(default='', max_length=20),
        ),
    ]
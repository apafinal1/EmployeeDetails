# Generated by Django 3.1 on 2020-08-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='end_time',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='start_time',
            field=models.DateTimeField(auto_created=True),
        ),
    ]

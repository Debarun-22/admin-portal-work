# Generated by Django 3.2.4 on 2021-07-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credential', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]

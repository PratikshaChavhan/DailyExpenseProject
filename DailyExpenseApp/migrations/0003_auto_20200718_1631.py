# Generated by Django 3.0.7 on 2020-07-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyExpenseApp', '0002_auto_20200718_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='income',
            field=models.IntegerField(),
        ),
    ]

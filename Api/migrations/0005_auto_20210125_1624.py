# Generated by Django 3.1.5 on 2021-01-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_donate_blood'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate_blood',
            name='Status',
            field=models.CharField(default='Pending', max_length=100),
        ),
        migrations.AddField(
            model_name='request_blood',
            name='Status',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]
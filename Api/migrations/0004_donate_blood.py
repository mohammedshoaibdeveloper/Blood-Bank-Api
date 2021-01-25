# Generated by Django 3.1.5 on 2021-01-25 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_auto_20210125_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate_Blood',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(default='First_Name', max_length=100)),
                ('Last_Name', models.CharField(default='Last_Name', max_length=100)),
                ('DOB', models.CharField(default='0/0/0', max_length=100)),
                ('Gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=100)),
                ('Bloodgroup', models.CharField(choices=[('O-', 'O-'), ('O+', 'O+'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='', max_length=100)),
                ('Address', models.CharField(default='Address', max_length=100)),
                ('Place_to_Donate', models.TextField(default='No')),
                ('User_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.signup')),
            ],
        ),
    ]
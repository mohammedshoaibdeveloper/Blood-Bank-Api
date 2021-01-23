from django.db import models
from rest_framework import serializers

Device = (

        ('ios','ios'),
        ('android','android'),
         ('web','web'),

    )


gender = (
        ('male','male'),
        ('female','female'),
    )

Bloodgroup = (
        ('O-','O-'),
        ('O+','O+'),
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        
    )


class Signup(models.Model):


    id = models.AutoField(primary_key=True)
    Full_Name=models.TextField(default="Full_Name")
    Email=models.EmailField(default="email@gmail.com")
    Username=models.TextField(default="Username")
    Password=models.TextField(default="Password")
    Location = models.CharField(max_length=100,default="Location")
    PhoneNumber = models.CharField(max_length=100,default="PhoneNumber")
    Gender = models.CharField(max_length=100,default="male",choices=gender)
    Bloodgroup = models.CharField(max_length=100,default="",choices=Bloodgroup)
    Image=models.ImageField(upload_to='Signup/',default="Health_Professional/dummy.jpg")
    Sender_ID = models.TextField(default="Sender_ID")
    Device_type = models.CharField(max_length=100,choices=Device,default="android")
    latitude = models.CharField(max_length=100,default="latitude")
    longitude = models.CharField(max_length=100,default="longitude")
    
   




    def __str__(self):
        return self.Full_Name


class SerSignup(serializers.ModelSerializer):
    class Meta:
        model = Signup
        
        fields = '__all__'
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
    Full_Name=models.CharField(max_length=100,default="Full_Name")
    Email=models.EmailField(max_length=100,default="email@gmail.com")
    Username=models.CharField(max_length=100,default="Username")
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





class Donate_Blood(models.Model):


    id = models.AutoField(primary_key=True)
    User_id=models.ForeignKey(Signup,on_delete=models.CASCADE,blank=True,null=True)
    First_Name=models.CharField(max_length=100,default="First_Name")
    Last_Name=models.CharField(max_length=100,default="Last_Name")
    DOB=models.CharField(max_length=100,default="0/0/0")
    Gender = models.CharField(max_length=100,default="male",choices=gender)
    Bloodgroup = models.CharField(max_length=100,default="",choices=Bloodgroup)
    Address = models.CharField(max_length=100,default="Address")
    Place_to_Donate = models.TextField(default="No")
    Donate_Blood_Status = models.CharField(max_length=100,default="Pending")
    
    def __str__(self):
        return self.First_Name

class SerDonate_Blood(serializers.ModelSerializer):
    class Meta:
        model = Donate_Blood
        
        fields = '__all__'




class Request_Blood(models.Model):


    id = models.AutoField(primary_key=True)
    User_id=models.ForeignKey(Signup,on_delete=models.CASCADE,blank=True,null=True)
    Blood_for = models.CharField(max_length=100,default="self")
    First_Name=models.CharField(max_length=100,default="First_Name")
    Last_Name=models.CharField(max_length=100,default="Last_Name")
    DOB=models.CharField(max_length=100,default="0/0/0")
    Gender = models.CharField(max_length=100,default="male",choices=gender)
    Bloodgroup = models.CharField(max_length=100,default="",choices=Bloodgroup)
    Address = models.CharField(max_length=100,default="Address")
    Message_to_Donor = models.TextField(default="No")
    Request_Blood_Status = models.CharField(max_length=100,default="Pending")
    Donor_id = models.ForeignKey(Donate_Blood,on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return self.First_Name


class SerRequest_Blood(serializers.ModelSerializer):
    class Meta:
        model = Request_Blood
        
        fields = '__all__'





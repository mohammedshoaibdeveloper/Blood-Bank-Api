from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from passlib.hash import django_pbkdf2_sha256 as handler
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Signup,SerSignup,Request_Blood,SerRequest_Blood,Donate_Blood,SerDonate_Blood
from fcm_django.models import FCMDevice
from django.db.models import Q
class User_Signup(APIView):

    def get(self,request):

        
        try:

            data = Signup.objects.all()
            serializer = SerSignup(data,many=True)
            message={

                'status' : True,
                'data':serializer.data

            }
            
             


            return Response(message)
        except:
            message={
                'status' : False,

            }
            return Response(message)




    def post(self , request):
        try:

       

            Full_Name=request.data.get('Full_Name')
            Email=request.data.get('Email')
            Username=request.data.get('Username')
            Location=request.data.get('Location')
            PhoneNumber=request.data.get('PhoneNumber')
            Gender=request.data.get('Gender')
            Bloodgroup=request.data.get('Bloodgroup')
            Password=request.data.get('Password')
            Password=handler.hash(Password)
            Sender_ID=request.data.get('Sender_ID')
            Device_type=request.data.get('Device_type')
            latitude=request.data.get('latitude')
            longitude=request.data.get('longitude')

            

            checkEmailExist = Signup.objects.filter(Email = Email)
            if checkEmailExist:
                message = {
                "status" : False,
                'message' : "Email Already Exist",

                }
                return Response(message)

            checkUserName = Signup.objects.filter(Username = Username)
            if checkUserName:
                message = {
                'status' : False,
                'message' : "UserName Already Exist",

                }
                return Response(message)

            checkPhoneNumber = Signup.objects.filter(PhoneNumber = PhoneNumber)
            if checkPhoneNumber:
                message = {
                'status' : False,
                'message' : "Mobile Number Already Exist",

                }
                return Response(message)


            data = Signup(Full_Name = Full_Name , Username = Username,Email = Email,Password = Password,Sender_ID = Sender_ID,Device_type= Device_type,latitude = latitude,longitude = longitude,Location=Location,PhoneNumber=PhoneNumber,Gender = Gender,Bloodgroup = Bloodgroup)
            data.save()

            userid = data.id

            try:

                fcm = FCMDevice(registration_id = Sender_ID,name = userid,type = Device_type)
                fcm.save()

            except:
                None

            fetch_userobeject = Signup.objects.get(Username = Username)
            serdata = SerSignup(fetch_userobeject)

            message = {

                "status" : True,
                "message" : "Account Created Successfully",
                "data" : serdata.data


            }

            return Response(message)


        except Exception as e:

            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)



###patient login

class Login(APIView):
    def post(self,request):
        try:

            Username=request.data.get('Username')
            Password=request.data.get('Password')
            Sender_ID = request.data.get('Sender_ID')
            Device_type = request.data.get('Device_type')
            latitude=request.data.get('latitude')
            longitude=request.data.get('longitude')

            authenticate = Signup.objects.filter(Username=Username)



            

            if authenticate:
                authenticate = authenticate[0]



                


                if handler.verify(Password,authenticate.Password):


                    authenticate.Sender_ID=Sender_ID
                    authenticate.Device_type=Device_type
                    authenticate.save()


                    id = authenticate.id


                    fcm = FCMDevice.objects.filter(name = id)
                    if fcm:
                        fcm = fcm[0]

                        

                    
                        fcm.registration_id = Sender_ID
                        fcm.type = Device_type
                        fcm.save()


                        userdata = SerSignup(authenticate)
                        message={
                        'status' : True,
                        'message':'Successfully Login',
                        'data' : userdata.data,


                        }

                        return Response(message)


                        
                    else:
                        pass

                else:
                    message={
                    'message':'Username or Password Does Not Match'
                }

                    return Response(message)

                

            else:

                message={
                        'message':'Username or Password Does Not Match'
                    }

                return Response(message)


        except Exception as e:
            message={
                    'status' : False,
                    'message': str(e)
                }
            return Response(message)





###PatientEditProfile
class EditProfile(APIView):
    def post(self,request):

        try:

            id = request.data.get('id')

            Full_Name=request.data.get('Full_Name',False)

            oldpassword = request.data.get('oldpassword',False)



            newpassword = request.data.get('newpassword',False)
            
            Image = request.FILES.get('Image',False)

            userObject = Signup.objects.get(id = id)



            if handler.verify(oldpassword,userObject.Password):

            

                

                if newpassword:
                    userObject.Password = handler.hash(newpassword)

                    userObject.save()


                if Full_Name:
                    userObject.Full_Name = Full_Name
                    userObject.save()



                if Image:
                    userObject.Image = Image
                    userObject.save()

                userdata = SerSignup(userObject)

                message = {
                'status' : True,
                'message' : "Edit Successfully",
                'data':userdata.data

                }


               
                return Response(message)

            else:

                message = {
                'status' : False,
                'message' : "Your Old Password Doesn't Match",
                

                }

                return Response(message)




        except Exception as e:
            Message={
                    'status' : False,
                    'message': str(e)
                }
            return Response(Message)




class requestBlood(APIView):


    def get(self,request):

        
        try:

            id=request.GET['id']
            data = Request_Blood.objects.get(User_id = id)
            serializer = SerRequest_Blood(data)
            message={

                'status' : True,
                'data':serializer.data

            }
            
             


            return Response(message)

        except:
            message={
                'status' : False,

            }
            return Response(message)




    def post(self , request):

        try:

       

            id=request.data.get('id')
            Blood_for=request.data.get('Blood_for')
            First_Name=request.data.get('First_Name')
            Last_Name=request.data.get('Last_Name')
            DOB=request.data.get('DOB')
            Gender=request.data.get('Gender')
            Bloodgroup=request.data.get('Bloodgroup')
            Address=request.data.get('Address')
            Message_to_Donor=request.data.get('Message_to_Donor')

            id = Signup.objects.get(id  = id)
            

            

            

            data = Request_Blood(User_id = id , Blood_for = Blood_for,First_Name = First_Name,Last_Name = Last_Name,DOB = DOB,Gender= Gender,Bloodgroup = Bloodgroup,Address = Address,Message_to_Donor=Message_to_Donor)
            data.save()

            

            message = {

                "status" : True,
                "message" : "Submit Blood Request Successfully",
                


            }

            return Response(message)


        except Exception as e:

            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)







class donateBlood(APIView):


    def get(self,request):

        
        try:

            id=request.GET['id']
            data = Donate_Blood.objects.get(User_id = id)
            serializer = SerDonate_Blood(data)
            message={

                'status' : True,
                'data':serializer.data

            }
            
             


            return Response(message)

        except:
            message={
                'status' : False,

            }
            return Response(message)




    def post(self , request):

        try:

       

            id=request.data.get('id')
            First_Name=request.data.get('First_Name')
            Last_Name=request.data.get('Last_Name')
            DOB=request.data.get('DOB')
            Gender=request.data.get('Gender')
            Bloodgroup=request.data.get('Bloodgroup')
            Address=request.data.get('Address')
            Place_to_Donate=request.data.get('Place_to_Donate')

            id = Signup.objects.get(id  = id)
            

            

            

            data = Donate_Blood(User_id = id ,First_Name = First_Name,Last_Name = Last_Name,DOB = DOB,Gender= Gender,Bloodgroup = Bloodgroup,Address = Address,Place_to_Donate=Place_to_Donate)
            data.save()

            

            message = {

                "status" : True,
                "message" : "Submit Donate Blood Data Successfully",
                


            }

            return Response(message)


        except Exception as e:

            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)





class MyBloodRequest(APIView):


    def post(self , request):

        try:

       

            id=request.data.get('id')
            First_Name=request.data.get('First_Name')
            Last_Name=request.data.get('Last_Name')
            DOB=request.data.get('DOB')
            Gender=request.data.get('Gender')
            Bloodgroup=request.data.get('Bloodgroup')
            Address=request.data.get('Address')
            Place_to_Donate=request.data.get('Place_to_Donate')

            id = Signup.objects.get(id  = id)
            


            data = Donate_Blood(User_id = id ,First_Name = First_Name,Last_Name = Last_Name,DOB = DOB,Gender= Gender,Bloodgroup = Bloodgroup,Address = Address,Place_to_Donate=Place_to_Donate)
            data.save()

            

            message = {

                "status" : True,
                "message" : "Submit Donate Blood Data Successfully",
                


            }

            return Response(message)


        except Exception as e:

            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)




class DonateBlood(APIView):




    def post(self , request):

        # try:

       

        requester_id=request.data.get('requester_id')
        donater_id=request.data.get('donater_id')

        donate_object = Donate_Blood.objects.get(User_id  = donater_id)
        requester_object = Request_Blood.objects.get(User_id = requester_id)

        Donate_Blood_Status = donate_object.Donate_Blood_Status

        Donate_Blood_object = Donate_Blood.objects.get(User_id = requester_id)


        

        if Donate_Blood_Status == "Donate":

            message = {

            "status" : False,
            "message" : "You are Already Donate Blood",
            


            }

            return Response(message)

        if donate_object.Bloodgroup ==  requester_object.Bloodgroup:

            donate_object.Donate_Blood_Status = "Donate"
            donate_object.save()

            requester_object.Request_Blood_Status="Donate"
            requester_object.Donor_id = Donate_Blood_object
            requester_object.save()







            message = {

            "status" : True,
            "message" : "Successfully Donate Blood",
            


            }

            return Response(message)


        else:


            message = {

                "status" : False,
                "message" : "Blood Group Doesn't Match",
                


                }

            return Response(message)

        


        
        # data.save()

        

        # message = {

        #     "status" : True,
        #     "message" : "Submit Donate Blood Data Successfully",
            


        # }

        # return Response(message)


        # except Exception as e:

        #     data={
        #             'status' : False,
        #             'message': str(e)
        #         }
        #     return Response(data)
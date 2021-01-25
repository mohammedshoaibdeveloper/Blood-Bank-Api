from django.urls import path,include
from Api.views import *





urlpatterns = [

    path('User_Signup',User_Signup.as_view()),
    path('Login',Login.as_view()),
    path('EditProfile',EditProfile.as_view()),
    path('requestBlood',requestBlood.as_view()),
    path('donateBlood',donateBlood.as_view()),
    path('MyBloodRequest',MyBloodRequest.as_view()),
    path('DonateBlood',DonateBlood.as_view()),




]
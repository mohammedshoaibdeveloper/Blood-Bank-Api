from django.contrib import admin
from .models import Signup,Request_Blood,Donate_Blood
# Register your models here.

admin.site.register(Signup)
admin.site.register(Request_Blood)
admin.site.register(Donate_Blood)

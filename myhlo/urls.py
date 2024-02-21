
from django.urls import path
from .views import index,about
from .views  import *

urlpatterns = [
    path('',index,name="index"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),
    path('post/',post,name="post"),
    path('userfrms/',userfrms,name="userfrms"),
    path('cals/',cals,name="cals"),
    path('evenodd/',evenodd,name="evenodd"),
    path('service/',service,name="service"),
  
]

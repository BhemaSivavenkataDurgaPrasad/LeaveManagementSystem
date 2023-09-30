from django.urls import path
from . import views

urlpatterns = [
     path('' , views.home , name = 'home' ),
     path('register/' , views.Register , name = "Principal_register"),
     path('login/' , views.login , name = "Principal_login"),
     path('phome//<int:id>' , views.phome , name = "phome"),
     path('login/pprofile//<int:id>' , views.pprofile , name = "pprofile"),
     path('login/pprofile//pprofileupdate//<int:id>' , views.pprofileupdate , name = "pprofileupdate"),
     path('login/pregister/' ,views.pregister ,name = "pregister"),
     path('login/Thistory/' , views.Thistory , name = "Thistory"),
     path('login/grant/' , views.grant , name = "grant"),
     path('login/grant/request//<int:id>' , views.request , name = 'request'),
      
]

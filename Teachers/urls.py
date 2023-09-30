
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Teacher_Home , name = "teacher_home"),
    path('login',views.login , name = "teacher_login"),
    path('register' , views.Register , name = "teacher_register"),
    path('Tprofile//<int:id>', views.Tprofile , name = "Tprofile" ),
    path('Tprofile//profileupdate//<int:id>' , views.profileupdate , name = "profileupdate"),
    path('LeaveFrom//<int:id>',views.LeaveFrom , name = "LeaveFrom"),
    path('Repassword//<int:id>', views.ResetPassword , name = "Repassword"),
    path("history//<int:id>" , views.History , name = "history")  
]

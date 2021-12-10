from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views  

urlpatterns = [
    path('' ,  home  , name="home"),
    path('register/' , register_attempt , name="register_attempt"),
    path('accounts/login/' , login_attempt , name="login_attempt"),
    path('token/' , token_send , name="token_send"),
    path('success/' , success , name='success'),
    path('verify/<auth_token>/' , verify , name="verify"),
    path('error/' , error_page , name="error"),
    path('logout/' , handleLogout , name="logout"),
    path('forget-password/' , ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , ChangePassword , name="change_password"),
    path('doctornew/' ,  doctornew  , name="doctornew"),
    path('blog/' ,  blog  , name="blog"),
    path('chatbot/' ,  chatbot , name="chatbot"),
    path('dp/' ,  dp , name="dp"),
    path('dp/end.html/' ,  end , name="end"),
    path('singleblog/' ,  singleblog  , name="singleblog"),

    
   
]
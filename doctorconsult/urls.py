#from django.contrib import admin
from django.urls import path, include
from . import views




urlpatterns = [
    
    
    path('appointment/<str:user_name>/',views.appointment,name='appointment'),
    path('doctor/',views.doctor),
    path('display/',views.display),
    path('doctordelete/<str:user_name>/', views.DeleteView.as_view(), name='doctordelete'),
    path('doctorprofile/<str:user_name>/', views.ProfileView.as_view(), name='doctorprofile'),
    path('patientprofile/', views.ProfileViewPatient.as_view(), name='patientprofile'),
    path('doctordetail/<str:user_name>/', views.doctor_detail_view, name='doctor_detail'),
    path('doctorlist/', views.DoctorListView.as_view()),
    path('upload_file/', views.UploadViewPatient, name='upload_file'),
    path('indexpay/', views.indexpay, name='indexpay'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('cartdelete/<str:user_name>/', views.DeleteCartView.as_view(), name='cartdelete'),
    path('generateinvoice/<int:pk>/', views.GenerateInvoice.as_view(), name = 'generateinvoice'),
    path('link/', views.link, name='link'),
    

]
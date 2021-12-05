from django.urls import path
from . import views

urlpatterns = [
   
    path('ques/', views.homePage, name='index'),
    path('new-question', views.newQuestionPage, name='new-question'),
    path('question/<int:id>', views.questionPage, name='question'),
    path('reply', views.replyPage, name='reply')
]

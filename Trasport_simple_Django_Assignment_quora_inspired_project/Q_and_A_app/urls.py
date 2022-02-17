from django.urls import path
from Q_and_A_app import views

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('', views.homePage, name='home'),
    path('new-question', views.newQuestionPage, name='new-question'),
    path('question/<int:id>', views.questionPage, name='question'),
    path('like/<int:pk>',views.LikeView,name='like_post')
    
]

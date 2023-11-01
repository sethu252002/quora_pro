from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('quora_app.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'), 
    path('', views.home, name='home'),
    path('post_question/', views.post_question, name='post_question'),
    path('post_answer/<int:question_id>/', views.post_answer, name='post_answer'),
    path('like_answer/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('accounts/login/',views.CustomLoginView.as_view(), name='Custom_login'),
]
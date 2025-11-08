from django.urls import path
from .import views
from django.contrib.auth.views import LoginView 


urlpatterns = [
    path('register/', views.register, name='register'), # URL pattern for user registration
    path('login/', LoginView.as_view(template_name='login.html'), name='login'), # URL pattern for user login using Django's built-in LoginView
    path('logout/', views.logout_view, name='logout'), # URL pattern for user logout
]
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from . import views

urlpatterns = []

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home', views.HomeView.as_view(), name='home'),
]

urlpatterns += [
    
    path('privacy', views.PrivacyView.as_view(), name='privacy'),
]
 
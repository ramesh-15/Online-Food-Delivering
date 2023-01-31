from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donar_home', views.donar_home, name='donar_home'),
    path('donatefood', views.donatefood, name='donatefood'),
    # path('viewrequest', views.viewrequest, name='viewrequest'),
    path('NGO_home', views.NGO_home, name='NGO_home'),

    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('login', views.loginview, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('changepwd', views.setpwd, name='changepwd'),
    path('editprofile', views.edituser, name='editprofile'),
]
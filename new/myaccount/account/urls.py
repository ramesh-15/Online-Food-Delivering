from django.urls import path
from account import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),



    path('donar_home', views.donar_home, name='donar_home'),
    path('donatefood', views.donatefood, name='donatefood'),
    path('request/<int:id>', views.NGOrequest, name='request'),
    path('NGO_home', views.NGO_home, name='NGO_home'),
    path('Cart_NGO', views.Cart_NGO, name='Cart_NGO'),
    path('NGORequest', views.NGORequest, name='NGORequest'),



    path('DonarCart', views.DonarCart, name='DonarCart'),
    path('DonarRequest', views.DonarRequest, name='DonarRequest'),


    path('NGOCancel/<int:id>', views.NGOCancel, name='NGOCancel'),
    path('DonarCancel/<int:id>', views.DonarCancel, name='DonarCancel'),
    path('DonarAccept/<int:id>', views.DonarAccept, name='DonarAccept'),
    path('Decline/<int:id>', views.Decline, name='Decline'),






    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('login', views.loginview, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('changepwd', views.setpwd, name='changepwd'),
    path('editprofile', views.edituser, name='editprofile'),
]
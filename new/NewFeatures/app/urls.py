from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),



    path('donar_home', views.donar_home, name='donar_home'),
    path('donatefood', views.donatefood, name='donatefood'),
    path('donateclothes', views.donateclothes, name='donateclothes'),
    path('donatehealth', views.donatehealth, name='donatehealth'),
    path('donatefootware', views.donatefootware, name='donatefootware'),
    path('request/<int:id>', views.NGOrequest, name='request'),
    path('NGO_home', views.NGO_home, name='NGO_home'),
    path('Cart_NGO', views.Cart_NGO, name='Cart_NGO'),
    path('NGORequest', views.NGORequest, name='NGORequest'),



    path('DonarCart', views.DonarCart, name='DonarCart'),
    path('DonarRequest', views.DonarRequest, name='DonarRequest'),


    path('NGOCancel/<int:id>', views.NGOCancel, name='NGOCancel'),
    path('DonarCancel/<int:id>', views.DonarCancel, name='DonarCancel'),
    path('ClothesCancel/<int:id>', views.ClothesCancel, name='ClothesCancel'),
    path('HealthCancel/<int:id>', views.HealthCancel, name='HealthCancel'),
    path('FootwareCancel/<int:id>', views.FootwareCancel, name='FootwareCancel'),
    path('DonarAccept/<int:id>', views.DonarAccept, name='DonarAccept'),
    path('Decline/<int:id>', views.Decline, name='Decline'),






    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('signup', views.DonarSignup, name='signup'),
    path('login', views.Donarlog, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('changepwd', views.setpwd, name='changepwd'),
    path('editprofile', views.edituser, name='editprofile'),
]
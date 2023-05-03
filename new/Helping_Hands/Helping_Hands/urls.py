"""Helping_Hands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenRefreshView
# # donation
router = DefaultRouter()
router.register('Food', DonationFood,basename='food')
router.register('Clothes', DonationClothes,basename='clothes')
router.register('Footwear', DonationFootwear,basename='footwear')
router.register('Stationary', DonationStationary,basename='stationary')
router.register('Gadget', DonationGadget,basename='gadget')

router.register('Health', DonationHealth,basename='health')
router.register('History', History,basename='History')


# router.register('profile',DonorProfile,basename = 'profile')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('signupvol/',SignUpViewVol.as_view(),name='signupvol'),
    # path('edituser/<int:pk>',EditUserView.as_view(),name='edituser'),
    path('change_password/<int:pk>',ChangePasswordView.as_view(),name='auth_change_password'),
    path('signin/',LoginView.as_view(),name='signin'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('profile/', DonorProfile.as_view(), name='profile'),
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/',include(router.urls)),
   
  
    path('auth/',include('rest_framework.urls',namespace='rest-framework'))
]

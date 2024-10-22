"""FoodApi URL Configuration

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
from django.urls import path, include
from app.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('Food', DonationFood,basename='food')
router.register('Clothes', DonationClothes,basename='clothes')
router.register('Footwear', DonationFootwear,basename='footwear')
router.register('Stationary', DonationStationary,basename='stationary')
router.register('Gadget', DonationGadget,basename='gadget')
router.register('Health', DonationHealth,basename='health')
router.register('History', History,basename='History')


urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/', include(router.urls)),
    path('signin',LoginView.as_view()),
  
    path('setpassword',SetPassword.as_view(),name='setpassword'),
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('DonationFood', DonationFood.as_view(), name='DonationFood'),
    # path('History/<int:pk>', History.as_view(), name='History'),
    path('profile/', DonorProfile.as_view(), name='profile'),
    path('profileupdate/', ProfileUpdate.as_view(), name='profileupdate'),
    path('profilelogout/', LogoutAPIView.as_view(), name='profilelogout'),

    path('api/',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest-framework'))
 
]


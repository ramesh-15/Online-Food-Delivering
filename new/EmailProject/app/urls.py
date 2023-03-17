from django.urls import path
from . import views
urlpatterns = [
    path('signup',views.DonarSignup,name = 'signup'),
    path('home',views.home,name='home'),
    path('log',views.Donarlog,name='log'),
    path('',views.base,name = 'base'),
  
]
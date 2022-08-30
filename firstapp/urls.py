from django.urls import path
from . import views 

# Create your views here.

urlpatterns = [
    path('home',views.home, name='home'), 
    path('',views.login, name='login'), 
    path('logout',views.logout,name='logout'),
]

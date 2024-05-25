
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.base, name='base'),
    path('', views.loginview, name='loginview'),
    
]

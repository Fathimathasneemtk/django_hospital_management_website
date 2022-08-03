from django.conf import settings
from django.urls import path,include
from django.views import View
from . import views
urlpatterns = [
     path('', views.index,name='home'),
     path('about/', views.about,name='about'),
     path('booking/', views.booking,name='booking'),
      path('doctors', views.doctors,name='doctors'),
       path('contact', views.contact,name='contact'),
        path('department', views.department,name='department'),


]
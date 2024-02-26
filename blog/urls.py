# from django.contrib import admin
from django.urls import path
from blog import views


urlpatterns = [
    path('',views.home,name='home'),
    path('',views.confection,name='confection'),
    path('',views.liste,name='liste'),
    path('',views.inscription,name='inscription'),
]

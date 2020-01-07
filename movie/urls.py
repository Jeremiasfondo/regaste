
from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('<int:pk>/', views.movie),
    path('payment/', views.pay ,name="payment"),
]

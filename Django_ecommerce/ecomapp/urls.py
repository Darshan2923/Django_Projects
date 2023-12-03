from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
path('',views.store,name='store'),
path('checkout/',views.checkout,name='checkout'),
path('cart/',views.cart,name='cart'),
]

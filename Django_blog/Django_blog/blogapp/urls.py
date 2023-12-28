from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register_page,name='register_page'),
    path('login/',views.login_page,name='login_page'),
]

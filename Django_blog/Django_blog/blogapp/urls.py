from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register_page,name='register_page'),
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_user,name='logout_user'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('profile_page/',views.profile_page,name='profile_page'),
]

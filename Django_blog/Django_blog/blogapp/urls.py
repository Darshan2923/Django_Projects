from django.urls import path
from . import views

urlpatterns = [
    #blogs
    path('',views.index,name='index'),

    #profile
    path('profile_page/',views.profile_page,name='profile_page'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),

    #user authentication
    path('register/',views.register_page,name='register_page'),
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_user,name='logout_user'),
]

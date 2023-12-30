from django.urls import path
from . import views

urlpatterns = [
    #blogs
    path('',views.index,name='index'),
     path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path('add_blogs/',views.add_blogs,name='add_blogs'),
    path('delete_blog_post/<str:slug>/',views.delete_blog_post,name='delete_blog_post'),

    #profile
    path('profile_page/',views.profile_page,name='profile_page'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),

    #user authentication
    path('register/',views.register_page,name='register_page'),
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_user,name='logout_user'),
]

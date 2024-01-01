from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('chat/',views.chat,name='chat'),
    path('notifications/',views.notifications,name='notifications'),
    path('quit/',views.quit,name='quit'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create_notes/',views.createNotes,name='create_notes'),
]
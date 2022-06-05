from django.urls import path 
from . import views

urlpatterns = [
    # manages root path/home page window
    path('',views.index, name = 'index'),
    # manages about window
    path('about',views.about, name = 'about')
]
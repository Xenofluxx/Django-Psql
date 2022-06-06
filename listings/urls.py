from django.urls import path 
from . import views

urlpatterns = [    
    path('',views.index, name = 'listings'), 
    # listing with number
    path('<int:listing_id>',views.listing, name = 'listing'),
    # will use seach from templates
    path('<search>',views.search, name = 'search')
]
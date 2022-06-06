from django.contrib import admin
from django.urls import path, include

# include, similar to import, used between urlsconfig
urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('listings/', include('listings.urls'))
]

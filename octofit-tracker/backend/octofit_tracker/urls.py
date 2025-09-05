from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api_urls')),
]

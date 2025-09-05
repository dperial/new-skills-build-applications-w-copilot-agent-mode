from django.contrib import admin
from django.urls import path, include
from octofit_tracker.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('octofit_tracker.api_urls')),
    ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('autoservice/', include('autoservice.urls')),
    path('admin/', admin.site.urls),
]
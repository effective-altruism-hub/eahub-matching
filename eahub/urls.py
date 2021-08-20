from django.contrib import admin
from django.urls import include
from django.urls import path

from eahub.api import api


urlpatterns = [
    path("api/", api.urls),
    path("admin/", admin.site.urls),
]

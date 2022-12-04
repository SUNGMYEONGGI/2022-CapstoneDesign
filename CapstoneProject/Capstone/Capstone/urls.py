from django.contrib import admin
from django.urls import path, include
from Test.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
]
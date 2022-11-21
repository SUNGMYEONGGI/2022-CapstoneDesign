from django.contrib import admin
from django.urls import path
from DjangoWeb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('createform/', views.createform, name='createform'),  # 데이터를 처리할 url 등록!
]
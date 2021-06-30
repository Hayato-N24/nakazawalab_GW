from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('templates/', views.index, name='index'),
    path('templates/', views.list_view, name='list_view'),
]

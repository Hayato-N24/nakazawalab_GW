from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.list_view, name='list_view'),
    ]

from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.list_view, name='list_view'),

    #ユーザの詳細情報を表示する処理を呼び出す
    path('<int:id>', views.showDetail, name='showDetail'),
 
    #ユーザの登録フォームを呼び出す
    path('create', views.showCreateUserForm, name='showCreateUserForm'),
    ]


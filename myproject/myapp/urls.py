from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.showUsers, name='showUsers'),

    #ユーザの詳細情報を表示する処理を呼び出す
    #path('<int:id>', views.showDetail, name='showDetail'),
    #ユーザの登録フォームを呼び出す
    path('create', views.showCreateUserForm, name='showCreateUserForm'),
    #ユーザ登録する処理を呼び出す
    path('add', views.addUser, name='addUser'),
    #ユーザ編集するフォームを呼び出す
    #path('<int:id>/edit', views.showEditUserForm, name='showEditUserForm'),
    path('searchForm', views.showSearchForm, name='searchForm'),
    path('searchResult', views.search, name='search'),
]
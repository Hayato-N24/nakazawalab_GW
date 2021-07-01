from django.shortcuts import render

from django.http import HttpResponse
from .models import UserInfo
from .forms import UserForm
# ユーザ情報を辞書に格納して、users.htmlに返す
def showUsers(request):
    usefinfo = UserInfo.objects.all()
    context = {
    'msg': '現在の利用状況',
    'userinfo': usefinfo,
    'count':usefinfo.count,
    }
    return render(request, 'myapp/users.html',context)


def showCreateUserForm(request):
    #フォームを変数にセット
    form = UserForm()
 
    context = {
        'userForm':form,
    }
 
    #detail.htmlへデータを渡す
    return render(request, 'myapp/create.html',context)

def addUser(request):
    #リクエストがPOSTの場合
    if request.method == 'POST':
        #リクエストをもとにフォームをインスタンス化
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            userForm.save()
 
    #登録後、全件データを抽出
    userinfo = UserInfo.objects.all()
    context = {
        'msg': '現在の利用状況',
        'userinfo': userinfo,
        'count':userinfo.count,
    }
 
    #user.htmlへデータを渡す
    return render(request, 'myapp/users.html',context)


def showEditUserForm(request,id):
 
    #idをもとにユーザ情報を取得
    userinfo = get_object_or_404(UserInfo,pk=id)
    #フォームをオブジェクトを作成
    userForm = UserForm(instance=userinfo)
    
    #ユーザ情報をフォームに格納
    context = {
        'userinfo':userinfo,
        'userForm':userForm,
    }
 
    #edit.htmlへデータを渡す
    return render(request, 'myapp/edit.html',context)



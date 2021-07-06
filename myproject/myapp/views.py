from django.shortcuts import redirect, render

from django.http import HttpResponse
from .models import UserInfo
from .forms import UserForm
#検索用モジュール
from django.contrib import messages
from django.db.models import Q
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
            messages.success(request, '登録できました。ログインしてください。')
        else:
            errorhtml = '<a href="create">戻る</a>'
            return HttpResponse('そのユーザーネームは既に使用されています。' + errorhtml)
 
    #登録後、全件データを抽出
    userinfo = UserInfo.objects.all()
    context = {
        'msg': '現在の利用状況',
        'userinfo': userinfo,
        'count':userinfo.count,
    }
 
    #user.htmlへデータを渡す
    return render(request, 'myapp/login.html',context)


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


def showSearchForm(request):
    return render(request, 'myapp/showSearchForm.html')

def searchResult(request):
    model = UserInfo.objects

    keyword = request.GET.get('keyword')

    if keyword is not None:
       
        model = model.filter(
            userName__iexact = keyword
        )
        if model.count() > 0:
            messages.success(request, "「{}」の検索結果".format(keyword))
        else:
            errorhtml = '<a href="searchForm">戻る</a>'
            return HttpResponse('該当のユーザーは存在しません' + errorhtml)
        
    
    return render(request, 'myapp/searchResult.html', {'result':model})

def login(request):
    model = UserInfo.objects
    keyword = request.GET.get('keyword')

    if keyword:   
        model = model.filter(
            userName__iexact = keyword
        )
        if model.count() == 1:
            return redirect('showSearchForm')
        else:
            messages.error(request, '登録されていません。')
        
    return render(request, 'myapp/login.html')
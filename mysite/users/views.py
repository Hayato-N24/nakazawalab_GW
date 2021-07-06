from django.shortcuts import render
from .forms import UserForm

# 新規登録フォームHTMLへ返す
def showCreateUserForm(request):
    #フォームを変数にセット
    form = UserForm()
 
    context = {
        'userForm':form,
    }
 
    #detail.htmlへデータを渡す
    return render(request, 'create.html',context)
# Create your views here.

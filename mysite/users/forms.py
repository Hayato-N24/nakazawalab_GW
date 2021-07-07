from django import forms
from . models import UserInfo
 
class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('userName', 'mailaddress', 'selfIntroduction', 'allergie')
        labels={
           'userName':'名前',
           'mailaddress':'メールアドレス',
           'selfIntroduction':'自己紹介',
           'allergie': 'アレルギー',
           }

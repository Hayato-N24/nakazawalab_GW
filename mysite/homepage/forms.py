
from django import forms
from . models import UserInfo
class UserForm(forms.ModelForm):
    class Meta:
        #model = UserInfo
        fields = ('userName', 'country','sex','address','selfIntroduction')
        labels={
        'userName':'名前',
        'country':'出身国',
        'address':'住所',
        'sex':'性別',
        'selfIntroduction':'自己紹介',
    }

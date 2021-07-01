from django import forms
from . models import UserInfo

class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('userName', 'allergy','like','dislike')
        labels={
           'userName':'名前',
           'allergy':'アレルギー',
           'like':'好きな食べ物',
           'dislike':'嫌いな食べ物',
           }
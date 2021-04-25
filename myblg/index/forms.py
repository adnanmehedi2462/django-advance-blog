from django import forms
from .models import artical,author,comment,categary
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CreateForm(forms.ModelForm):
    class Meta:
        model= artical
        fields=[
            

            'title','body','categary','image',


        ]

class createfrom(UserCreationForm):
    class Meta:
        model = User
        fields=[
            'first_name', 'last_name','username', 'email','password1','password2',
        ]
class createauthor(forms.ModelForm):
    class Meta:
        model=author
        fields=[
            'details',
            'profile_pic',

        ]
class createcomment(forms.ModelForm):
    class Meta:
        model=comment
        fields=[
            'Name',
            'email',
            'post_comment',




        ]
class createcategory(forms.ModelForm):
    class Meta:
        model=categary
        fields=[
            'name',

        ]
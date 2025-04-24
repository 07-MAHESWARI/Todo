from django import forms

from django.forms import ModelForm

from myapp.models import User, TaskModel  # table is user

class UserRegForm(forms.ModelForm):

    class Meta:

        model = User  # user table (model) is used here

        fields = ["username","password","email","first_name"]

    
class LoginForm(forms.Form):

    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)


class TaskForm(forms.ModelForm):

    class Meta:

        model = TaskModel

        exclude = ["created_date","complete_status","user_id"]
        # these 3 is not input by user


class ForgotPassForm(forms.Form):

    email = forms.CharField(max_length=50)
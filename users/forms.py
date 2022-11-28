from django import forms
from .models import Users

class Userform(forms.ModelForm):
    class Meta:
        model = Users
        widgets = {
        'password': forms.PasswordInput(),
        'confirmpassword': forms.PasswordInput(),
    }
        fields =[
            'username','name','email','password','confirmpassword','types'
        ]
    
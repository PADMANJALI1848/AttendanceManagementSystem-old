from django import forms
from .models import Users 
from django.forms import ValidationError

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

    
    
    def clean(self):
        super(Userform, self).clean()
        email=self.cleaned_data.get("email")
        password=self.cleaned_data.get("password")
        confirmpassword=self.cleaned_data.get("confirmpassword")
        if email.endswith("@bmsce.ac.in"):
            raise ValidationError("This is not a valid password.")
        if not confirmpassword == password:
            raise ValidationError("This is not a valid password.")

        return self.cleaned_data
        
    
    
    
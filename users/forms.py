from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class NewRegisterFrom(UserCreationForm):
    email=forms.EmailField(required=True,widget=forms.EmailInput (attrs={'placeholder':'Enter your Email','class':'form-control'}))
    username=forms.CharField(required=True ,widget=forms.TextInput (attrs={'placeholder':'Enter yor Username','class':'form-control'}))
    password1=forms.CharField(required=True ,label='Passowrd',widget=forms.PasswordInput (attrs={'placeholder':'Enter 8 digit password','class':'form-control'}))
    password2=forms.CharField(required=True,label='Re-enter password',widget=forms.PasswordInput (attrs={'placeholder':'Enter 8 digit password','class':'form-control'}))

    class Meta:
        model=User
        fields={"username","email","password1","password2"}
    
    def save(self,commit=True):
        user=super(NewRegisterFrom,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit :
            user.save()
        return user
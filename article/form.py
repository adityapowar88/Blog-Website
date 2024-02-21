from django import forms
from django.forms import ModelForm
from .models import Article



class ArticleForms(forms.ModelForm):
    class  Meta:
        model= Article
        fields=('title','content','image')
        widgets={
            # 'category' : forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'rows':'8', 'cols':'10','class':'form-control'}),  
        }   
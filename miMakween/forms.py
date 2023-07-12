from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

    
class NuevoUsuario(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    foto = forms.ImageField(required=True)

    def __init__(self, *args, **kwargs):
        super(NuevoUsuario, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta():
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','foto']



        

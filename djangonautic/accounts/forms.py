from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Userform(UserCreationForm):

    mobilenumoremial= forms.EmailField(widget= forms.TextInput
                           (attrs={'placeholder':'mobile number or emial'}))




    class Meta:
        model = User
        fields= ('mobilenumoremial','username','password1','password2')
    def __init__(self, *args, **kwargs):
        super(Userform,self).__init__(*args, **kwargs)
        self.fields['mobilenumoremial'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder']='username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder']='password'
        self.fields['password2'].widget.attrs['placeholder']='password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

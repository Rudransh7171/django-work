from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


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
class CustomAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')
    def __init__(self, *args, **kwargs):
        super(CustomAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'})
        self.fields['password'].label = False

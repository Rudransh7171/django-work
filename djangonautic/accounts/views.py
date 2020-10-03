from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import Userform



# Create your views here.



def signup_view(request):
    if request.method == 'POST':
        form = Userform(request.POST)

        if form.is_valid():
            user=form.save()
            return redirect('accounts:login')
    else:
        form = Userform()
    return render(request,'accounts/signup.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('articles:list')

    else:
        form = AuthenticationForm()
    return render(request,"accounts/login.html",{'form':form})


def logout_view(request):
    if request.method =="POST":
        logout(request)
        return redirect('accounts:login')

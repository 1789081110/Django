from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserReisterForm
from .forms import UserUpdateForm
from .forms import ProfilePicForm
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method=='POST':
        form=UserReisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'the register is completed {username} you can login now!!')
            return redirect('login')
    else:
        form=UserReisterForm()    
    return render(request,'users/register.html',{'form':form})
from django import forms
@login_required
def profile(request):
    if request.method=='POST':
        u_form= UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfilePicForm(request.POST,request.FILES,instance=request.user.profile)
       
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account is Updated')
            return redirect('profile')
            
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form=ProfilePicForm(instance=request.user.profile)
        

    context={
        'u_form':u_form,'p_form':p_form
    }
    return render(request,'users/profile.html',context)
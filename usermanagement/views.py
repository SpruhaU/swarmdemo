from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserForm

#login form
def home(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            # Handle successful login
            return redirect('user_list')
    else:
        login_form = AuthenticationForm()

    return render(request, 'usermanagement/home.html', {'login_form': login_form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'usermanagement/user_list.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'usermanagement/add_user.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

# Create your views here.

# 🔐 Вход
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('games_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# 🚪 Выход
def logout_view(request):
    logout(request)
    return redirect('login')

# 📝 Регистрация
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('games_list')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})
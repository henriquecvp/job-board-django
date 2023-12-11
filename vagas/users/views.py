from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Sucesso!')
            return redirect('job_list')
        else:
            messages.success(request,'Erro! Tente novamente.')
            return redirect('Login')

    else:
        return render(request, 'loginscreen.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('Login')

def create_user(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        first_name = request.POST['first_name']
        password = request.POST['password']
        company = request.POST['company'] == 'yes'

        user = CustomUser.objects.create_user(username=username, first_name=first_name, password=password, company=company)

        if user is not None:
            messages.success(request,'Sucesso!')
            return redirect('Login')
        else:
            messages.success(request,'Erro! Tente novamente.')
            return redirect('Signup')

    else:
        return render(request, 'signupscreen.html', {})












        

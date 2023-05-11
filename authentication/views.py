from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def create_user(request):
    if request.user.is_authenticated or not list(User.objects.all()):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            User.objects.create_user(username=username, email=email, password=password, is_superuser=True)
            return redirect('product:products')
        else:
            return render(request, 'create-user.html')
    else:
        return redirect('authentication:login')


def login_user(request):
    if list(User.objects.all()):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('product:products')
            else:
                print("Invalid login details")
                return render(request, 'login.html', {'error_message': 'Invalid login details'})
        return render(request, "sign-up.html")
    else:
        return redirect('authentication:create_user')


@login_required(login_url='authentication:login')
def logout_user(request):
    logout(request)
    return redirect('authentication:login')

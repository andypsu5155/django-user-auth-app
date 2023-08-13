from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return redirect('error-login')

    return render(request, 'user_auth_app/login_user.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        new_user = User.objects.create_user(username, email, password)
        new_user.save()

        return redirect('home')

    return render(request, 'user_auth_app/register.html', {})

def error_login(request):
    return render(request, "user_auth_app/error_login.html", {})
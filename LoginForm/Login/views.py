from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import *
from django.contrib.auth import logout


def index(request):
    return render(request, 'login/index.html')


def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'login/authentication/registration.html', context)


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('index')

    context = {}

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')
        else:
            context['login_form'] = form
    else:
        form = LoginForm()
        context['login_form'] = form

    return render(request, 'login/authentication/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def account_view(request):

    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial={
                'email': request.user.email,
                'username': request.user.username,
            }
        )

    context['account_form'] = form
    return render(request, 'login/authentication/account.html', context)









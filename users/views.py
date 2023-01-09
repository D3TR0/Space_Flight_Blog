from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, login, authenticate
from .forms import UserRegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    # Logged in user can't register a new account
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request = request,
        template_name = "register.html",
        context={"form":form}
        )

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = AuthenticationForm()

    return render(
        request=request,
        template_name="login.html",
        context={'form': form}
    )
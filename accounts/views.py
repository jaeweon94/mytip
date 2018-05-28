from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save() #user로 return하니깐, 근데 user에도 profile이 연결되어있으니 괜찮음.
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html', { 'form': form, })


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
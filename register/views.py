from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def register_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            register = form.save(commit=False) # forms.py에서 model = Register 해줬기 때문에 register는 Register 모델을 갖고 있음.
            register.user = request.user
            register.save()
            messages.success(request, '글이 등록되었습니다')
            return redirect('register:register_complete')
    else:
        form = RegisterForm()

    return render(request, 'register/register_form.html', {'form': form,})


def register_complete(request):
    return render(request, 'register/register_complete.html')


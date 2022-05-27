from django.shortcuts import render, redirect

def home(request):
    return redirect('/sign-up')

def sign_up_view(request):
    return render(request, 'index.html')
from django.shortcuts import render, redirect



def Forget(request):
    return render(request, 'reset-password.html')
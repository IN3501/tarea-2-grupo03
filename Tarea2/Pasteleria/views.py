from django.shortcuts import render

from .forms import loginForm


# Create your views here.
def login(request):
    return render(request,'Pasteleria/login.html')


def tryLogin(request):
    # if this is a POST request we need to process the form data
    nombre=request.POST["nombre"]
    print(nombre)
    return render(request,'Pasteleria/home.html', {'p':nombre})
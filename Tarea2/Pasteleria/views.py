from django.shortcuts import render

from .forms import loginForm


# Create your views here.
def login(request):
    return render(request,'Pasteleria/login.html')


def tryLogin(request):
    # if this is a POST request we need to process the form data
    datos = []
    datos.append(request.POST["nombre"])
    return render(request,'Pasteleria/home.html', {'llaveDatos':datos})

def home(request):
    return render(request,'Pasteleria/home.html')

def formularioCarla(request):
    return render(request,'Pasteleria/formularioCarla.html')

def formularioDiego(request):
    return render(request,'Pasteleria/formularioDiego.html')

def registro(request):
    return render(request,'Pasteleria/registrarse.html')

def tryRegistrar(request):
    datos=[]
    datos.append(request.POST["nombre"])
    datos.append(request.POST["correo"])
    datos.append(request.POST["telefono"])
    return render(request,'Pasteleria/home.html', {'llaveDatos':datos})

def recuperar(request):
    porcion=request.POST["inputPorciones"]
    base=request.POST["inputBase"]
    cobertura=request.POST["inputCobertura"]
    diccionario={}
    diccionario["PORCIONES"]=porcion
    diccionario["BASE"]=base
    diccionario["COBERTURA"]=cobertura
    return render(request, "mostrar_resultado.html", diccionario)
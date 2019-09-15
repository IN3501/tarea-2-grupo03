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

    print(request.POST)
    rellenos=[]
    for k in request.POST.keys():

        if request.POST[k]=='on':

            rellenos.append(k)
    print(rellenos)
    diccionario["RELLENO"]=rellenos


    return render(request, "Pasteleria/mostrar_resultado.html", diccionario)


    #if "snack" in request.POST:
    #    comida.append(request.POST["snack"])
    #if "bebida" in request.POST:
    #    comida.append(request.POST["bebida"])
    #print("comida")

def compraExitosa(request):
    print(request.POST)

    compras=[]
    for keyCompra in request.POST.keys():
        if keyCompra!='csrfmiddlewaretoken'  and request.POST[keyCompra]!="":
            compras.append([keyCompra,request.POST[keyCompra]])

    print(compras)
    return render(request, "Pasteleria/compraExitosa.html",{'compras':compras})
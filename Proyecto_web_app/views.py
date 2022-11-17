from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):

    return render(request, 'inicio.html')

def Servicos(request):

    return render(request, 'servicios.html')

def Tienda(request):

    return render(request, 'tienda.html')

def Blog(request):

    return render(request, 'blog.html')

def Contacto(request):

    return render(request, 'contactos.html')
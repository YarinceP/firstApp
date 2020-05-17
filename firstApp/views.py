from django.http import HttpResponse

def saludo(request): #first view
    return HttpResponse("Hola mundo desde mi primera pagina en Django")
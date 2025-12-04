from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contato(request):
    pagina = '<body><h1><center>Kassiano Alves</center></h1></body>'
    return HttpResponse(pagina)

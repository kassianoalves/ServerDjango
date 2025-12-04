from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    lista = '<ol><li>Kassiano</li><li>Pedru</li><li>Marcone</li></ol>'
    return HttpResponse(lista)
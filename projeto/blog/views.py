from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    print('Passei no blog')
    #return HttpResponse('<body bgcolor="lightblue"><h1>Bem-vindo ao meu blog!</h1></body>')
    return render(
        request, 
        'blog/index.html', {'title': 'Blog'})

def artigo(request):
    return render(
        request, 
        'blog/artigo.html', {'title': 'Artigo'})
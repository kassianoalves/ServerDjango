from django.http import HttpResponse
import socket
def home(request):
    hostname = socket.gethostname() # Obtém o nome do host do servidor onde a aplicação está rodando.
    message = f'Olá, visitante de {hostname}! - Create by Kassiano' # Mensagem personalizada com o nome do host.
    return HttpResponse(message)
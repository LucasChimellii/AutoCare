from django.shortcuts import render
from .models import Servico
def pagina_inicial(request):
    placa_digitada = request.GET.get('placa')

    placa_formatada = placa_digitada.replace('-', '').upper() # Garante que a placa digitada seja formatada para busca no banco de dados
    servico_encontrado = None

    if placa_digitada:
        servico_encontrado = Servico.objects.filter(carro__placa__iexact= placa_formatada).first
        
    contexto = {
        'servico': servico_encontrado,
        'placa_buscada': placa_formatada,
    }

    return render(request, 'gestao/home.html', contexto)
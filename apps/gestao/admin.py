from django.contrib import admin
from .models import Cliente, Carro, Servico, FotoAvaria
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from django.db.models import Sum, Avg, Count, Q

admin.site.register(Carro)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'telefone']
    list_display = ['nome', 'telefone', 'email']


class FotoAvariaInline(admin.TabularInline):
    model = FotoAvaria
    extra = 5


class ServicoAdmin(admin.ModelAdmin):
    list_display = ('carro', 'get_placa', 'status_servico', 'data_entrada', 'valor', 'botao_whatsapp')
    list_filter = ('status_servico',)
    readonly_fields = ('botao_whatsapp',)
    inlines = [FotoAvariaInline]

    def get_placa(self, obj):
        return obj.carro.placa
    get_placa.short_description = 'Placa'
    get_placa.admin_order_field = 'carro__placa'


    def botao_whatsapp(self, obj):
        numero = obj.carro.cliente.get_whatsapp_number()
        nome = obj.carro.cliente.nome
        veiculo = f"{obj.carro.marca} {obj.carro.modelo}"
        status = obj.status_servico

        if status == 'CONCLUIDO':
            link = f"https://wa.me/{numero}?text=Olá {nome}! O serviço no seu {veiculo} foi concluído na AutoCare. Já pode vir buscar! 🚗"

            return format_html(
                '<a style="background-color: #28a745; color: white; padding: 5px 10px; border-radius: 4px; text-decoration: none; font-weight: bold;" href="{}" target="_blank">📲 Avisar Cliente (Concluído) </a>',
                link
            )


        elif status ==  'EM ANDAMENTO':
            link = f"https://wa.me/{numero}?text=Olá {nome}! O serviço no seu {veiculo} foi iniciado na AutoCare. Daqui a pouquinho te daremos mais informações! 🚗"

            return format_html(
                '<a style="background-color: #28a745; color: white; padding: 5px 10px; border-radius: 4px; text-decoration: none; font-weight: bold;" href="{}" target="_blank">📲 Avisar Cliente (Serviço iniciado) </a>',
                link
            )

        return "-"

    botao_whatsapp.short_description = 'Notificação'



    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        # Deixa apenas o botão "Salvar" nativo do Django
        context['show_save_and_add_another'] = False
        context['show_save_and_continue'] = False
        context['show_history'] = False
        context['show_close'] = False

        return super().render_change_form(request, context, add, change, form_url, obj)

        #Quando edita um serviço existente
    def response_change(self, request, obj):

        response = super().response_change(request, obj)
        if "_save" in request.POST:
            return HttpResponseRedirect(request.path)
        return response

    # Quando cria um serviço do zero pela primeira vez
    def response_add(self, request, obj, post_url_continue=None):
        response = super().response_add(request, obj, post_url_continue)
        # Se clicou em "Salvar", redireciona direto para a tela de edição desse novo serviço
        if "_save" in request.POST:
            return HttpResponseRedirect(f"../{obj.pk}/change/")
        return response

    def changelist_view(self, request, extra_context=None):
        # 1. Fazemos os cálculos direto no Banco de Dados
        stats = Servico.objects.aggregate(
            total_faturado=Sum('valor', filter=Q(status_servico='CONCLUIDO')),
            ticket_medio=Avg('valor', filter=Q(status_servico='CONCLUIDO')),
            carros_na_fila=Count('id', filter=Q(status_servico='NA FILA')),
            carros_em_servico=Count('id', filter=Q(status_servico='EM ANDAMENTO'))
        )

        # 2. Empacotar esses cálculos para mandar para a interface visual depois
        extra_context = extra_context or {}
        extra_context['stats'] = stats

        return super().changelist_view(request, extra_context=extra_context)



admin.site.register(Servico, ServicoAdmin)





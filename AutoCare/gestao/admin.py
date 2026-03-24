from django.contrib import admin
from .models import Cliente, Carro, Servico, FotoAvaria

admin.site.register(Cliente)
admin.site.register(Carro)

class FotoAvariaInline(admin.TabularInline):
    model = FotoAvaria
    extra = 5


class ServicoAdmin(admin.ModelAdmin):
    list_display = ('carro', 'status_servico', 'data_entrada', 'valor')
    list_filter = ('status_servico',)
    inlines = [FotoAvariaInline]
    
admin.site.register(Servico, ServicoAdmin)



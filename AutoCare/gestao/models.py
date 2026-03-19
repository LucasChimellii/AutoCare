from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    cliente = models.ForeignKey (Cliente, on_delete=models.CASCADE)
    placa = models.CharField(max_length = 8)
    modelo = models.CharField(max_length = 100)
    marca = models.CharField(max_length = 50, null=True, blank=True)
    ano = models.IntegerField()

    def save(self, *args, **kwargs):
        # Converte automaticamente quando cadastrado no banco de dados para um formato de placa geral 
        if self.placa:
            self.placa = self.placa.replace('-', '').replace(' ', '').strip().upper()
            
        # E Salva no banco de dados
        super().save(*args, **kwargs)


    def __str__(self):
        return (f'{self.marca} - {self.modelo}')
    
class Servico(models.Model):
    carro = models.ForeignKey (Carro, on_delete=models.CASCADE)
    status_servico = models.CharField(max_length = 100, default= 'Na Fila')
    valor = models.DecimalField(max_digits = 8, decimal_places =2)
    descricao = models.CharField(max_length=200, null=True, blank= True)
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_saida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return (f'{self.carro}, {self.carro.cliente}, {self.carro.placa}, {self.status_servico}, {self.data_entrada}')

class FotoAvaria(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='avarias/')
    descricao = models.CharField(max_length = 100)


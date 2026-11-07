from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Cor(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class PecaDeRoupa(models.Model):
    OPCOES_TAMANHO = [
        ('P', 'Pequeno (P)'),
        ('M', 'Médio (M)'),
        ('G', 'Grande (G)'),
        ('GG', 'Extra Grande (GG)'),
    ]

    nome = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=2, choices=OPCOES_TAMANHO)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='roupas/', blank=True, null=True)
    
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    cores = models.ManyToManyField(Cor, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.tamanho}"

class Estoque(models.Model):
    peca = models.OneToOneField(PecaDeRoupa, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Estoque: {self.peca.nome} ({self.quantidade} un.)"
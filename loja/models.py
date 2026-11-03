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
    nome = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=5)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    
    #  1:N
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    
    # N:N 
    cores = models.ManyToManyField(Cor, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.tamanho}"

class Estoque(models.Model):
    #  1:1 
    peca = models.OneToOneField(PecaDeRoupa, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Estoque: {self.peca.nome} ({self.quantidade} un.)"
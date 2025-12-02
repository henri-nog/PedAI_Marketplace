from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='produtos/', blank=True, null=True)
    disponibilidade = models.BooleanField(default=True)  

    def __str__(self):
        return self.nome

from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_validade = models.DateTimeField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
       return self.nome

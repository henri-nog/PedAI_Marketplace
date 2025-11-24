from django.db import models


class Produto(models.Model):
    # id_usuario = models.AutoField(primary_key=True) 
    # nome = models.CharField(max_length=100)
    # email = models.EmailField()
    # idade = models.IntegerField()
    # curso = models.CharField(max_length=100)
    # data_cadastro = models.DateTimeField(auto_now_add=True)

    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
       return self.nome

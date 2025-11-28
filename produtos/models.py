from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, blank=True)
    idade = models.IntegerField()
    curso = models.CharField(max_length=100)

    def __str__(self) -> str:
       return self.nome

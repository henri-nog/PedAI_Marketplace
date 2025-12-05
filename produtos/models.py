from django.db import models
import qrcode
from django.core.files.base import ContentFile
from io import BytesIO
from django.utils.timezone import now

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='produtos/', blank=True, null=True)
    disponibilidade = models.BooleanField(default=True)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    comprador = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=20,
        choices=[
            ('pendente', 'Pendente'),
            ('confirmado', 'Confirmado'),
            ('cancelado', 'Cancelado'),
        ],
        default='pendente'
    )

    data = models.DateTimeField(default=now)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def gerar_qrcode(self):
        dados = f"Pedido {self.id} - Produto: {self.produto.nome}"
        img = qrcode.make(dados)

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        filename = f"pedido_{self.id}.png"

        self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)

    def save(self, *args, **kwargs):
        criando = self.pk is None  

        super().save(*args, **kwargs)  
       
       
        if criando and not self.qr_code:
            self.gerar_qrcode()
            super().save(*args, **kwargs)


    def __str__(self):
        return f"Pedido #{self.id} - {self.comprador}"
    


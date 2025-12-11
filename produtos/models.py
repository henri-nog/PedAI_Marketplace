from django.db import models                    # módulo de modelos do Django
import qrcode                                   # gera imagens de QR Code
from io import BytesIO                          # cria um arquivo em memória
from django.core.files.base import ContentFile  # transformar o arquivo gerado em memória em um que pode ser salvo no banco
from django.utils.timezone import now           # data e hora atual

# organiza os produtos
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)                    # não pode ter dois produtos com o mesmo nome
    descricao = models.TextField(blank=True)                                # no formulário, pode ficar vazio
    preco = models.DecimalField(max_digits=10, decimal_places=2)            
    foto = models.ImageField(upload_to="produtos/", blank=True, null=True)  # armazena a imagem do produto
    disponibilidade = models.BooleanField(default=True)                     # produto está disponível para venda                        

    # relacionamento com a Categoria
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL, # se a categoria for apagada, o produto não é apagado; a categoria vira null
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    comprador = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE) # Cada pedido está ligado a um produto. Se o produto for apagado, o pedido também é apagado
    quantidade = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=20,
        choices=[
            ("pendente", "Pendente"),
            ("confirmado", "Confirmado"),
            ("cancelado", "Cancelado"),
        ],
        default="pendente"
    )

    data = models.DateTimeField(default=now)                                    
    qr_code = models.ImageField(upload_to="qrcodes/", blank=True, null=True)

    # calcula o valor total do pedido
    def valor_total(self):
        return self.quantidade * self.produto.preco

    # todas as informações importantes do pedido & transformado em um QR Code
    def gerar_qrcode(self):
        dados = (
            f"PEDIDO #{self.id}\n"           # número do pedido
            f"Comprador: {self.comprador}\n"
            f"Produto: {self.produto.nome}\n"
            f"Quantidade: {self.quantidade}\n"
            f"Total: R$ {self.valor_total()}\n"
            f"Status: {self.status}\n"
            f"Data: {self.data.strftime('%d/%m/%Y %H:%M')}"
        )

        img = qrcode.make(dados)        # cria a imagem do QR Code
        buffer = BytesIO()              # cria um arquivo em memória, temporário
        img.save(buffer, format="PNG")  # salva dentro do buffer 

        filename = f"pedido_{self.id}.png"
        self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False) # salva o QR Code no campo qr_code & em media/qrcodes/

    # quando o QR Code deve ser gerado
    def save(self, *args, **kwargs):
        novo = self.pk is None          # verifica se o pedido está sendo criado pela primeira vez
        super().save(*args, **kwargs)   # salvamento normal do pedido

        if novo and not self.qr_code:   # se o pedido for novo e ainda não tiver QR Code, então gere um QR Code
            self.gerar_qrcode()
            super().save(update_fields=["qr_code"]) # salva só o qr_code no banco 

    def __str__(self):
        return f"Pedido #{self.id} - {self.comprador}"

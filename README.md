# 🖥️ Desenvoldor:


### Fellipe Nogueira Caluête

___

# Sobre o projeto

PedAI – Marketplace de Reservas Locais

Contexto:

Pequenos produtores, ambulantes e cozinheiros caseiros enfrentam dificuldades em controlar estoque e pedidos feitos informalmente via mensagens.

Proposta:

Criar um marketplace comunitário onde vendedores locais possam divulgar seus produtos, gerenciar
estoque e receber reservas com horário definido. O sistema deve gerar QR codes para confirmação,
permitir avaliações pós-compra e oferecer um painel de controle segmentado por bairro.

Lógica da Aplicação (CRUD e Relacionamentos):

● Usuário: autenticação (vendedor, comprador).

● Produto: CRUD (nome, preço, foto, descrição, disponibilidade, vendedor).

● Pedido: CRUD (comprador, produtos, status, data, QR code).

● Avaliação: CRUD vinculado ao pedido.

● Estoque: atualização automática após reserva.

● Dashboard: total de vendas, reservas e bairros com maior movimentação.

___

# Para rodar o projeto 


### Se tiver o arquivo ‘venv’: 

 ```bash
.\venv\Scripts\activate 
```
 ```bash
python .\manage.py migrate
```
**Em seguida:** 

 ```bash
python .\manage.py runserver 
```
 
### Se não houver: 

 ```bash
python -m venv venv 
```
 ```bash
.\venv\Scripts\activate 
```
 ```bash
python .\manage.py migrate
```

**Em seguida:** 

 ```bash
python .\manage.py runserver 
```

# Instruções de instalação:
 
 * Biblioteca para manipular imagens.

 ```bash
pip install Pillow
```

 * Biblioteca que gera QR Codes.

 ```bash
 pip install qrcode[pil]
 ```


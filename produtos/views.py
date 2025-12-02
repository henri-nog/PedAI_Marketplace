from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

# Listagem de todos os produtos
def listar_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})


# Cadastrar novo produto
def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        preco = request.POST['preco']
        disponibilidade = 'disponibilidade' in request.POST  
        foto = request.FILES['foto'] if 'foto' in request.FILES else None # Faz uma requisição pela foto, se não tiver, atribui como 'None'

        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco=preco,
            disponibilidade=disponibilidade,
            foto=foto
        )

        return redirect('listar_produto')

    return render(request, 'produtos/adicionar.html')


# Editar produto existente
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.descricao = request.POST['descricao']
        produto.preco = request.POST['preco']
        produto.disponibilidade = 'disponibilidade' in request.POST

        if 'foto' in request.FILES: 
            produto.foto = request.FILES['foto']

        produto.save()
        return redirect('listar_produto')

    return render(request, 'produtos/editar.html', {'produto': produto})


# Excluir produto
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listar_produto')

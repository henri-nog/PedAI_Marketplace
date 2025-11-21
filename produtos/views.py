from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
# Create your views here.


# Listagem de todos os elementos da classe produtos
def listar_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})


# Cadastrar itens da classe produtos
def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        quantidade = request.POST['quantidade']
        preco = request.POST['preco']
        data_validade = request.POST['data_validade']
        data_cadastro = request.POST['data_validade']
        Produto.objects.create(nome=nome, quantidade=quantidade,
                               preco=preco, data_validade=data_validade,
                               data_cadastro=data_cadastro)
        return redirect('listar_produto')
    return render(request, 'produtos/adicionar.html')


# Alterar itens da classe produtos
def editar_produto(request):
    produtos = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produtos.nome = request.POST['nome']
        produtos.quantidade = request.POST['quantidade']
        produtos.preco = request.POST['preco']
        produtos.data_validade = request.POST['data_validade']
        produtos.data_cadastro = request.POST['data_validade']
        Produto.objects.save()
        return redirect('listar_produto')
    return render(request, 'produtos/alterar.html')


# Excluir itens da classe produtos
def exluir_produto():
    produtos = get_object_or_404(Produto, id)
    produtos.delete()
    return redirect('listar_produto')

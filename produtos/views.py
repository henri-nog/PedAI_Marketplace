from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria, Pedido
from django.utils.timezone import now
import unicodedata
from django.db.models import Q


def listar_produto(request):
    termo = request.GET.get('busca')
    categoria_filtro = request.GET.get('categoria')
    ordem = request.GET.get('ordem')

    queryset = Produto.objects.all()

    if termo:
        termo_normalizado = remover_acentos(termo)

        ids_filtrados = [
            p.id
            for p in queryset
            if termo_normalizado in remover_acentos(p.nome)
        ]

        queryset = Produto.objects.filter(id__in=ids_filtrados)

    if categoria_filtro:
        queryset = queryset.filter(categoria_id=categoria_filtro)


    if ordem == "az":
        queryset = queryset.order_by('nome')
    elif ordem == "za":
        queryset = queryset.order_by('-nome')
    elif ordem == "menor_preco":
        queryset = queryset.order_by('preco')
    elif ordem == "maior_preco":
        queryset = queryset.order_by('-preco')

    categorias = Categoria.objects.all()

    return render(request, 'produtos/listar.html', {
        'produtos': queryset,
        'categorias': categorias,
        'categoria_filtro': categoria_filtro,
        'termo': termo,
        'ordem': ordem
    })

def remover_acentos(texto):
    if not texto:
        return ""
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()


def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        preco = request.POST['preco']
        disponibilidade = 'disponibilidade' in request.POST
        
        foto = request.FILES.get('foto')

        categoria_id = request.POST.get('categoria')
        categoria = Categoria.objects.get(id=categoria_id) if categoria_id else None

        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco=preco,
            disponibilidade=disponibilidade,
            foto=foto,
            categoria=categoria
        )

        return redirect('listar_produto')

    categorias = Categoria.objects.all()
    return render(request, 'produtos/adicionar.html', {'categorias': categorias})

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

    categorias = Categoria.objects.all()
    return render(request, 'produtos/editar.html', {
        'produto': produto,
        'categorias': categorias
    })

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listar_produto')

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar.html', {'categorias': categorias})


def adicionar_categoria(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        Categoria.objects.create(nome=nome)
        return redirect('listar_categorias')
    return render(request, 'categorias/adicionar.html')


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.nome = request.POST['nome']
        categoria.save()
        return redirect('listar_categorias')
    return render(request, 'categorias/editar.html')


def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('listar_categorias')

def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/listar.html', {'pedidos': pedidos})


def adicionar_pedido(request):
    produtos = Produto.objects.all()

    if request.method == "POST":
        comprador = request.POST.get("comprador")
        produto_id = request.POST.get("produto")
        quantidade = int(request.POST.get("quantidade", 1))

        produto = get_object_or_404(Produto, id=produto_id)

        Pedido.objects.create(
            comprador=comprador,
            produto=produto,
            quantidade=quantidade
        )
        
        return redirect('listar_pedidos')

    return render(request, 'pedidos/adicionar.html', {'produtos': produtos})


def editar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        pedido.status = request.POST['status']
        pedido.save()
        return redirect('listar_pedidos')

    return render(request, 'pedidos/editar.html', {'pedido': pedido})


def excluir_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    return redirect('listar_pedidos')


def detalhes_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    return render(request, 'pedidos/detalhes.html', {'pedido': pedido})

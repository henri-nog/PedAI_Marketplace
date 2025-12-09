from django.urls import path
from . import views

urlpatterns = [

    # HOME
    path("home/", views.home, name="home"),

    # PRODUTOS
    path("", views.listar_produto, name="listar_produto"),
    path("adicionar/", views.adicionar_produto, name="adicionar_produto"),
    path("editar/<int:id>/", views.editar_produto, name="editar_produto"),
    path("excluir/<int:id>/", views.excluir_produto, name="excluir_produto"),
    path("produto/<int:id>/", views.detalhes_produto, name="detalhes_produto"),

    # CATEGORIAS
    path("categorias/", views.listar_categorias, name="listar_categorias"),
    path("categorias/adicionar/", views.adicionar_categoria, name="adicionar_categoria"),
    path("categorias/editar/<int:id>/", views.editar_categoria, name="editar_categoria"),
    path("categorias/excluir/<int:id>/", views.excluir_categoria, name="excluir_categoria"),

    # PEDIDOS
    path("pedidos/", views.listar_pedidos, name="listar_pedidos"),
    path("pedidos/adicionar/", views.adicionar_pedido, name="adicionar_pedido"),
    path("pedidos/editar/<int:id>/", views.editar_pedido, name="editar_pedido"),
    path("pedidos/excluir/<int:id>/", views.excluir_pedido, name="excluir_pedido"),
    path("pedidos/<int:id>/", views.detalhes_pedido, name="detalhes_pedido"),
]

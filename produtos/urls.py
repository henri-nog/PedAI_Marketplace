from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produto, name='listar_produto'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('excluir/<int:id>/', views.exluir_produto, name='exluir_produto')
]

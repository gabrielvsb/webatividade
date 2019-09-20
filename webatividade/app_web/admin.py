from django.contrib import admin
from .models import Pessoa
from .models import Categoria
from .models import Funcionario
from .models import Produto
from .models import Cliente
from .models import Venda

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    pass
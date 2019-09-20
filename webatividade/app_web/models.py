from django.db import models


class Categoria(models.Model):
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    nome = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    nome = models.CharField(max_length=128)
    preco = models.FloatField()
    qtd = models.IntegerField()
    categoria = models.ForeignKey('Categoria')

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    """
    Description: Model Description
    """

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    nome = models.CharField(max_length=128)
    data_nasc = models.DateField(auto_now=False, auto_now_add=False)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


class Funcionario(Pessoa):
    codFunc = models.CharField(max_length=5)

    def __str__(self):
        return self.nome


class Cliente(Pessoa):

    def __str__(self):
        return self.nome


class Venda(models.Model):

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"

    cliente = models.ForeignKey(Cliente, on_delete=None)
    funcionario = models.ForeignKey(Funcionario, on_delete=None)
    Produto = models.ForeignKey(Produto, on_delete=None)
    data = models.DateField(auto_now=True)

    def __str__(self):
        nome = str(self.Produto)+ ' - ' + str(self.data)
        return nome

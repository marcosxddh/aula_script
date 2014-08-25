# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from produto_app.model import Produto

class ProdutoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Produto
    _include = [Produto.price, 
                Produto.quantidade, 
                Produto.descricao, 
                Produto.nome]


class ProdutoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Produto
    _include = [Produto.price, 
                Produto.quantidade, 
                Produto.descricao, 
                Produto.nome]


class ProdutoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Produto
    _include = [Produto.price, 
                Produto.creation, 
                Produto.quantidade, 
                Produto.descricao, 
                Produto.nome]


class ProdutoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Produto
    _include = [Produto.price, 
                Produto.creation, 
                Produto.quantidade, 
                Produto.descricao, 
                Produto.nome]


class SaveProdutoCommand(SaveCommand):
    _model_form_class = ProdutoForm


class UpdateProdutoCommand(UpdateNode):
    _model_form_class = ProdutoForm


class ListProdutoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListProdutoCommand, self).__init__(Produto.query_by_creation())


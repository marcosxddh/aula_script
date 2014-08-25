# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from servico_app.model import Servico

class ServicoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Servico
    _include = [Servico.preco, 
                Servico.descricao, 
                Servico.nome]


class ServicoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Servico
    _include = [Servico.preco, 
                Servico.descricao, 
                Servico.nome]


class ServicoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Servico
    _include = [Servico.creation, 
                Servico.preco, 
                Servico.descricao, 
                Servico.nome]


class ServicoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Servico
    _include = [Servico.creation, 
                Servico.preco, 
                Servico.descricao, 
                Servico.nome]


class SaveServicoCommand(SaveCommand):
    _model_form_class = ServicoForm


class UpdateServicoCommand(UpdateNode):
    _model_form_class = ServicoForm


class ListServicoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListServicoCommand, self).__init__(Servico.query_by_creation())


# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from produto_app.commands import ListProdutoCommand, SaveProdutoCommand, UpdateProdutoCommand, \
    ProdutoPublicForm, ProdutoDetailForm, ProdutoShortForm


def save_produto_cmd(**produto_properties):
    """
    Command to save Produto entity
    :param produto_properties: a dict of properties to save on model
    :return: a Command that save Produto, validating and localizing properties received as strings
    """
    return SaveProdutoCommand(**produto_properties)


def update_produto_cmd(produto_id, **produto_properties):
    """
    Command to update Produto entity with id equals 'produto_id'
    :param produto_properties: a dict of properties to update model
    :return: a Command that update Produto, validating and localizing properties received as strings
    """
    return UpdateProdutoCommand(produto_id, **produto_properties)


def list_produtos_cmd():
    """
    Command to list Produto entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListProdutoCommand()


def produto_detail_form(**kwargs):
    """
    Function to get Produto's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ProdutoDetailForm(**kwargs)


def produto_short_form(**kwargs):
    """
    Function to get Produto's short form. just a subset of produto's properties
    :param kwargs: form properties
    :return: Form
    """
    return ProdutoShortForm(**kwargs)

def produto_public_form(**kwargs):
    """
    Function to get Produto'spublic form. just a subset of produto's properties
    :param kwargs: form properties
    :return: Form
    """
    return ProdutoPublicForm(**kwargs)


def get_produto_cmd(produto_id):
    """
    Find produto by her id
    :param produto_id: the produto id
    :return: Command
    """
    return NodeSearch(produto_id)


def delete_produto_cmd(produto_id):
    """
    Construct a command to delete a Produto
    :param produto_id: produto's id
    :return: Command
    """
    return DeleteNode(produto_id)


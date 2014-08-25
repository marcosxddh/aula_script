# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from produto_app import facade
from routes.produtos import admin


@no_csrf
def index(produto_id):
    produto = facade.get_produto_cmd(produto_id)()
    detail_form = facade.produto_detail_form()
    context = {'save_path': router.to_path(save, produto_id), 'produto': detail_form.fill_with_model(produto)}
    return TemplateResponse(context, 'produtos/admin/form.html')


def save(_handler, produto_id, **produto_properties):
    cmd = facade.update_produto_cmd(produto_id, **produto_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'produto': cmd.form}

        return TemplateResponse(context, 'produtos/admin/form.html')
    _handler.redirect(router.to_path(admin))


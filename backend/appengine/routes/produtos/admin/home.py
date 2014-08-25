# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from produto_app import facade
from routes.produtos.admin import new, edit


def delete(_handler, produto_id):
    facade.delete_produto_cmd(produto_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_produtos_cmd()
    produtos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.produto_short_form()

    def short_produto_dict(produto):
        produto_dct = short_form.fill_with_model(produto)
        produto_dct['edit_path'] = router.to_path(edit_path, produto_dct['id'])
        produto_dct['delete_path'] = router.to_path(delete_path, produto_dct['id'])
        return produto_dct

    short_produtos = [short_produto_dict(produto) for produto in produtos]
    context = {'produtos': short_produtos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)


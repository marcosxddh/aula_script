# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from produto_app import facade


def index():
    cmd = facade.list_produtos_cmd()
    produto_list = cmd()
    short_form=facade.produto_short_form()
    produto_short = [short_form.fill_with_model(m) for m in produto_list]
    return JsonResponse(produto_short)


def save(**produto_properties):
    cmd = facade.save_produto_cmd(**produto_properties)
    return _save_or_update_json_response(cmd)


def update(produto_id, **produto_properties):
    cmd = facade.update_produto_cmd(produto_id, **produto_properties)
    return _save_or_update_json_response(cmd)


def delete(produto_id):
    facade.delete_produto_cmd(produto_id)()


def _save_or_update_json_response(cmd):
    try:
        produto = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.produto_short_form()
    return JsonResponse(short_form.fill_with_model(produto))


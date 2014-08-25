# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from servico_app import facade


def index():
    cmd = facade.list_servicos_cmd()
    servico_list = cmd()
    short_form=facade.servico_short_form()
    servico_short = [short_form.fill_with_model(m) for m in servico_list]
    return JsonResponse(servico_short)


def save(**servico_properties):
    cmd = facade.save_servico_cmd(**servico_properties)
    return _save_or_update_json_response(cmd)


def update(servico_id, **servico_properties):
    cmd = facade.update_servico_cmd(servico_id, **servico_properties)
    return _save_or_update_json_response(cmd)


def delete(servico_id):
    facade.delete_servico_cmd(servico_id)()


def _save_or_update_json_response(cmd):
    try:
        servico = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.servico_short_form()
    return JsonResponse(short_form.fill_with_model(servico))


# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from servico_app import facade
from routes.servicos import admin


@no_csrf
def index(servico_id):
    servico = facade.get_servico_cmd(servico_id)()
    detail_form = facade.servico_detail_form()
    context = {'save_path': router.to_path(save, servico_id), 'servico': detail_form.fill_with_model(servico)}
    return TemplateResponse(context, 'servicos/admin/form.html')


def save(_handler, servico_id, **servico_properties):
    cmd = facade.update_servico_cmd(servico_id, **servico_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'servico': cmd.form}

        return TemplateResponse(context, 'servicos/admin/form.html')
    _handler.redirect(router.to_path(admin))


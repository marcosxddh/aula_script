# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from servico_app import facade
from routes.servicos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'servicos/admin/form.html')


def save(_handler, servico_id=None, **servico_properties):
    cmd = facade.save_servico_cmd(**servico_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'servico': cmd.form}

        return TemplateResponse(context, 'servicos/admin/form.html')
    _handler.redirect(router.to_path(admin))


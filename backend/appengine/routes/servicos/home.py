# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from servico_app import facade
from routes.servicos import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_servicos_cmd()
    servicos = cmd()
    public_form = facade.servico_public_form()
    servico_public_dcts = [public_form.fill_with_model(servico) for servico in servicos]
    context = {'servicos': servico_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)


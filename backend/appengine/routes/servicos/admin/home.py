# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from servico_app import facade
from routes.servicos.admin import new, edit


def delete(_handler, servico_id):
    facade.delete_servico_cmd(servico_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_servicos_cmd()
    servicos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.servico_short_form()

    def short_servico_dict(servico):
        servico_dct = short_form.fill_with_model(servico)
        servico_dct['edit_path'] = router.to_path(edit_path, servico_dct['id'])
        servico_dct['delete_path'] = router.to_path(delete_path, servico_dct['id'])
        return servico_dct

    short_servicos = [short_servico_dict(servico) for servico in servicos]
    context = {'servicos': short_servicos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)


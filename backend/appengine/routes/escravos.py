# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from escravo_app import facade as escravo_facade
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission import facade
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(_logged_user):
    busca = escravo_facade.listar_escravos_de_dono(_logged_user)

    escravos = busca()
    escravo_form_short = escravo_facade.escravo_form_short()
    escravos = [escravo_form_short.fill_with_model(e) for e in escravos]
    editar_form_path = router.to_path(editar_form)
    deletar_path = router.to_path(deletar)
    for e in escravos:
        e['editar_path'] = '%s/%s' % (editar_form_path, e['id'])
        e['deletar_path'] = '%s/%s' % (deletar_path, e['id'])

    context = {'lista_de_escravos': escravos}
    return TemplateResponse(context)


def deletar(escravo_id):
    deletar_cmd = escravo_facade.deletar_escravos_cmd(escravo_id)
    deletar_cmd()
    return RedirectResponse(router.to_path(index))


@no_csrf
def editar_form(escravo_id):
    escravo_por_id_cmd = escravo_facade.get_escravo_por_id_cmd(escravo_id)
    escravo = escravo_por_id_cmd()
    escravo_form = escravo_facade.escravo_form()
    escravo_form.fill_with_model(escravo)
    contexto = {'salvar_path': router.to_path(editar, escravo_id),
                'escravo': escravo_form}
    return TemplateResponse(contexto, 'escravos/form.html')


def editar(escravo_id, **kwargs):
    editar_escravo_cmd = escravo_facade.editar_escravo_cmd(escravo_id, **kwargs)
    try:
        editar_escravo_cmd()
        return RedirectResponse(router.to_path(index))
    except CommandExecutionException:
        contexto = {'salvar_path': router.to_path(editar),
                    'escravo': kwargs,
                    'erros': editar_escravo_cmd.errors}
        return TemplateResponse(contexto, 'escravos/form.html')


@no_csrf
def form():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)


def salvar(email_dono, **kwargs):
    cmd = facade.get_user_by_email(email_dono)
    salvar_dono_de_escravo =  escravo_facade.salvar_escravo(cmd,**kwargs)
    try:
        salvar_dono_de_escravo.execute()
        return RedirectResponse(router.to_path(index))
    except CommandExecutionException:
        contexto = {'salvar_path': router.to_path(salvar),
                    'escravo': kwargs,
                    'erros': salvar_dono_de_escravo.errors}
        return TemplateResponse(contexto, 'escravos/form.html')

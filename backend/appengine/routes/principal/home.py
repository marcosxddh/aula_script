# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index(nome='Renzo', sobrenome='Nuccitelli'):

    class Pessoa(object):
        def __init__(self, nome, sobrenome):
            self.nome = nome
            self.sobrenome = sobrenome

    pessoas = [Pessoa('Renzo', 'Nuccitelli'), Pessoa('Giovane', 'Liberato')]


    contexto = {'name': nome, 'lastname':sobrenome, 'pessoas':pessoas}
    return TemplateResponse(contexto)

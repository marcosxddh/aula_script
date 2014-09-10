from google.appengine.ext import ndb
from gaecookie.decorator import no_csrf

__author__ = 'marcos'


@no_csrf
def listar():
    query = Escravo.query()

    escravos = query.fetch()#filtros  .order(Escravo.none)
    escravos = [form_short.fill_with_model(e) for e in escravos]
    for e in escravos:
        e['edit_path'] = router.to_path(edit_form, e['id'])
        e['delete_path'] = router.to_path(deletar, e['id'])
    contexto = {'escravos': escravos}
    return TemplateResponse(contexto)

def deletar(escravo_id):
    key = ndb.Key(Escravo, int(escravo_id))
    key.delete()
    return RedirectResponse(router.to_path(listar))

@no_csrf
def index():
    contexto={'salvar_path': router.to.path(salvar)}
    return templateResponse(contexto)


class Escravo(ndb.Model):
    bith=ndb.DateProperty()#pegar a data atual
    creation = ndb.DateProperty(auto_now=True)
    age=ndb.IntegerProperty()
    name=ndb.StringProperty(required=True)



@no_csrf
def edit_form(escravo_id):
    escravo = Escravo.get_by_id(int(escravo_id))
    escravo_form = EscravoForm()
    escravo_form.fill_with_model(escravo)
    contexto = {'salvar_path': router.to_path(salvar), 'escravo':escravo_form}
    return TemplateRespose(contexto,'db/home.html')


def editar(escravo_id, **kwargs):
    escravo_form = EscravoForm(**kwargs)
    erros = escravo_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(editar, escravo_id),
                    'erros':erros,
                    'escravo': kwargs}
        return TemplateResponse(contexto, 'db/home.html')
    else:
        escravo = Escravo.get_by_id(escravo_id)
        escravo = escravo_form.fill_model(escravo)
        escravo.put()
        return RedirectResponse(router.to(listar))



class EscravoForm(base.Form, ModelForm):
    _model_class = Escravo
    _exclude = [Escravo.bith]
    _include = [Escravo.name]

    email = EmailField(required=True)

    bith=base.DateField()
    age=base.IntegerField()
    name=base.StringField()



def salvar(_resp, **kwargs):
    escravo_form = EscravoForm(**kwargs)
    erros=escravo_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'erros':erros,
                    'escravo': kwargs}
        return TemplateResponse(contexto, 'db/home.html')
    else:
        campos = escravo_form.normalize()
        escravo = Escravo(**campos)
        escravo.put()
        return RedirectResponse(router.to(listar))

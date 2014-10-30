# -*- coding: utf-8 -*-
from google.appengine.ext import ndb
from gaeforms.ndb.form import ModelForm
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaegraph.model import Node, Arc
from tekton import router
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(_logged_user):
    produtos = Produto.query()
    contexto={'produto': produtos}
    return TemplateResponse(contexto)


'''

    chave_usuario = _logged_user.key
    query = UsuarioArco.query(UsuarioArco.origin==chave_usuario)
    usuario = query.fetch()
    chave_produto = [u.destination for u in usuario]
    produto_lista = ndb.get_multi(chave_produto)
'''

@no_csrf
def editar_form(produto_id):
    codigo = int(produto_id)
    query = Produto.get_by_id(codigo)
    contexto={'editar_path': router.to_path(editar), 'produto': query}
    return TemplateResponse(contexto, 'produto/form.html')


def excluir(produto_id):
    codigo = int(produto_id)
    produto = Produto.get_by_id(codigo)
    produto.status = '0'
    produto.put()


@no_csrf
def form():
    contexto={'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)


class Produto(Node):
    nome=ndb.StringProperty(required=True)
    descricao=ndb.StringProperty(required=True)
    preco=ndb.StringProperty(required=True)
    modelo=ndb.StringProperty(required=True)
    status=ndb.StringProperty(default="1")


class ProdutoForm(ModelForm):
    _model_class = Produto
    _exclude = [Produto.creation]
    #_include = [Produto.nome, Produto.descricao, Produto.preco, Produto.modelo]


class UsuarioArco(Arc):
    origin = ndb.KeyProperty(required=True)
    destination = ndb.KeyProperty(Produto, required=True)


@no_csrf
def salvar(_resp, **propriedades):
    produtoForm=ProdutoForm(**propriedades)

    erros=produtoForm.validate()
    if erros:
        _resp.status_code = 500
        return JsonUnsecureResponse(erros)
        #return TemplateResponse(contexto, 'produto/form.html')
    else:
        produto = produtoForm.fill_model()
        produto.put()
        return JsonUnsecureResponse(produto.to_dict())
        #return RedirectResponse(router.to_path(index))


@no_csrf
def editar(**propriedades):
    produtoForm=ProdutoForm(**propriedades)
    erros=produtoForm.validate()
    if erros:
        contexto={'salvar_path': router.to_path(salvar),
                  'produto': produtoForm,
                  'erros': erros}
        return TemplateResponse(contexto, 'produto/form.html')
    else:
        produto = produtoForm.fill_model(produtoForm)
        produto.put()
        return RedirectResponse(router.to_path(index))
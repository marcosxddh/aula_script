# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Produto(Node):
    nome = ndb.StringProperty(required=True)
    descricao = ndb.StringProperty(required=True)
    price = property.SimpleCurrency(required=True)
    quantidade = ndb.IntegerProperty(required=True)


# -*- coding: utf8 -*-
from flask import Blueprint
from flask_restplus import Api
from namespaces import api as netnsdao

blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(blueprint,
          title='Vrouter Api',
          doc='/doc/',
          version='1.0',
          )

api.add_namespace(netnsdao)

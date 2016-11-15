from flask_restplus import Namespace, Resource, fields, abort
from pyroute2 import NetNS, netns

api = Namespace('netnamespaces', description='Network namespace')

nsnetns = api.model('Netns_model', {
    'netns': fields.String,
})


@api.route('/')
class NetNamespaces(Resource):
    @api.doc('lest network namespaces')
    @api.response(200, 'Success')
    def get(self):
        namespaces = netns.listnetns()
        return namespaces


@api.route('/<string:nspath>')
@api.doc(params={'nspath': 'a namespace name'})
class NetNamespace(Resource):
    @api.marshal_with(nsnetns)
    @api.response(200, 'Success')
    @api.response(404, 'Namespace does not exist')
    def get(self, nspath):
        if nspath in netns.listnetns():
            namespace = NetNS(nspath)
            return namespace
        else:
            abort(404, "Namespace " + nspath + " does not exist")

    def post(self, nspath):
        if nspath in netns.listnetns():
            abort(500, "Namespace already exists")
        else:
            NetNS(nspath)

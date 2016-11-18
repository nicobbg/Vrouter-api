from flask_restplus import Namespace, Resource, abort
from pyroute2 import NetNS, netns
from models.model_netns import NetnsDao, model_netns
from models.model_interface import model_interface

# Create a namespace
nsnetns = Namespace('netnamespaces', description='Network namespace')

# Register models
nsnetns.models[model_netns.name] = model_netns
nsnetns.models[model_interface.name] = model_interface


# Create routes to work with the resource
@nsnetns.route('/')
class NetNamespaces(Resource):
    @nsnetns.doc('List network namespaces')
    @nsnetns.response(200, 'Success')
    def get(self):
        return netns.listnetns()


@nsnetns.route('/<string:nspath>')
@nsnetns.doc(params={'nspath': 'a network namespace name'})
class NetNamespace(Resource):

    @nsnetns.marshal_with(model_netns)
    @nsnetns.doc('Retrieve a network namespace detail')
    @nsnetns.response(200, 'Network namespace detail')
    @nsnetns.response(404, 'Namespace does not exist')
    def get(self, nspath):
        if nspath in netns.listnetns():
            return NetnsDao(nspath)
        else:
            abort(404, "Namespace " + nspath + " does not exist")

    def put(self, nspath):
        if nspath not in netns.listnetns():
            abort(404, "Namespace not found")
        else:
            pass

    @nsnetns.doc('Create a network namespace')
    @nsnetns.response(200, 'Network namespace successfully created')
    @nsnetns.response(500, 'Network namespace already exists')
    def post(self, nspath):
        if nspath in netns.listnetns():
            abort(500, "Namespace already exists")
        else:
            mynet = NetNS(nspath)
            mynet.close()
            return("Namespace successfully created")

    @nsnetns.doc('Delete a network namespace')
    @nsnetns.response(200, 'Network namespace successfully removed')
    @nsnetns.response(404, 'Network namespace not found')
    def delete(self, nspath):
        if nspath not in netns.listnetns():
            abort(404, "Namespace not found")
        else:
            mynet = NetNS(nspath)
            mynet.remove()
            mynet.close()
            return("Namespace successfully removed")


@nsnetns.route('/<string:nspath>/interfaces')
class NetNsIp(Resource):
    @nsnetns.marshal_with(model_interface)
    @nsnetns.doc('List namespace interfaces')
    @nsnetns.response(200, 'Returns the list of interface with their ip')
    @nsnetns.response(404, 'Namespace does not exist')
    def get(self, nspath):
        if nspath in netns.listnetns():
            return NetnsDao(nspath).get_interfaces_dao()
        else:
            abort(404, "Namespace does not exist")

    def put(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

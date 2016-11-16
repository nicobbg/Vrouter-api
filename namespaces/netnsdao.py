from flask_restplus import Namespace, Resource, fields, abort
from pyroute2 import IPDB, NetNS, netns

# Create a namespace
nsnetns = Namespace('netnamespaces', description='Network namespace')

# Create a model for my resource
model_netns = nsnetns.model('Netns_model', {
    'netns': fields.String,
})

model_ip = nsnetns.model('Interface_model', {

})


# Create routes to work with the resource
@nsnetns.route('/')
class NetNamespaces(Resource):
    @nsnetns.doc('List network namespaces')
    @nsnetns.response(200, 'Success')
    def get(self):
        namespaces = netns.listnetns()
        return namespaces


@nsnetns.route('/<string:nspath>')
@nsnetns.doc(params={'nspath': 'a network namespace name'})
class NetNamespace(Resource):
    @nsnetns.marshal_with(model_netns)
    @nsnetns.doc('Retrieve a network namespace detail')
    @nsnetns.response(200, 'Success')
    @nsnetns.response(404, 'Namespace does not exist')
    def get(self, nspath):
        if nspath in netns.listnetns():
            namespace = NetNS(nspath)
            return namespace
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


@nsnetns.route('/<string:nspath>/ips')
@nsnetns.doc(params={'nspath': 'a network namespace name'})
class NetNsIp(Resource):
    @nsnetns.doc('List namespace ip')
    @nsnetns.response(404, 'Namespace does not exist')
    def get(self, nspath):
        if nspath in netns.listnetns():
            interface = ()
            ips = []
            ipdb = IPDB(nl=NetNS(nspath))
            for i in ipdb.interfaces.iteritems():
                interface = (i[0], i[1].ipaddr)
                ips.append(interface)
            return ips
        else:
            abort(404, "Namespace " + nspath + " does not exist")

    def put(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

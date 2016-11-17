from flask_restplus import Model, fields
from pyroute2 import IPDB, NetNS
from model_interface import InterfaceDao

# Create a model for my resource
model_netns = Model('Netns_model', {
    'netns': fields.String,
})


class NetnsDao():
    def __init__(self, nspath):
        self.name = nspath
        self.interfaces = self.get_interfaces()

    def get_interfaces(self):
        interfaces = []
        with IPDB(nl=NetNS(self.name)) as ipdb:
            for i in ipdb.interfaces.iteritems():
                interface = InterfaceDao(i[1])
                interfaces.append(interface)
        return interfaces

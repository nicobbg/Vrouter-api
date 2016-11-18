from flask_restplus import Model, fields
from pyroute2 import IPDB, NetNS
from model_interface import InterfaceDao

# Create a model for my resource
model_netns = Model('Netns_model', {
    'name': fields.String,
    'interfaces_name': fields.List(fields.String)
})


class NetnsDao():
    '''
    The NetnsDao class provides the short representation of a network namespace

    :attr name: the name of the namespace
    :attr interfaces: the list of interfaces in the namespace
    :param nspath: the name of the namespace
    :type nspath: string
    '''
    def __init__(self, nspath):
        self.name = nspath
        self.interfaces_name = []
        for i in self.get_interfaces_dao():
            self.interfaces_name.append(i.ifname)

    def get_interfaces_dao(self):
        '''
        This method retrieves the list of interfaces for the network namespace.
        It will returns a list of InterfaceDao object.

        :returns: list of interfaces in the namespace
        :rtype: list of :class:InterfaceDao
        '''
        interfaces = []
        with IPDB(nl=NetNS(self.name)) as ipdb:
            for i in ipdb.interfaces.iteritems():
                interface = InterfaceDao(i[1])
                interfaces.append(interface)
        return interfaces

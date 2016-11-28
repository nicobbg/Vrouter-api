from flask_restplus import Model, fields
from pyroute2 import IPDB, NetNS
from model_interface import InterfaceDao

# Create a model for my resource
model_netns = Model('Netns_model', {
    'name': fields.String,
    'interfaces': fields.List(fields.String)
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
        self.interfaces = self.get_interfaces()

    def get_interfaces(self):
        '''
        This method retrieves the list of interfaces for the network namespace.

        :returns: list of interfaces in the namespace
        :rtype: list
        '''
        interfaces = []
        with IPDB(nl=NetNS(self.name)) as ipdb:
            for i in ipdb.interfaces:
                if type(i) is str:
                    interfaces.append(i)
        return interfaces

    def create_interface(self, iftype, ifname):
        '''This method create an interface in the network namespace.

        :param iftype: the interface type (bridge, vlan, veth)
        :type iftype: string
        :param ifname: the interface name
        :type ifname: string
        '''
        pass

    def set_interface(self):
        pass

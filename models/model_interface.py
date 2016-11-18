from flask_restplus import Model, fields

model_interface = Model('Interface_model', {
    'ifname': fields.String,
    'ip': fields.String,
    'status': fields.String
})


class InterfaceDao():
    '''
    The InterfaceDao class provides the short representation of
    a network interfaces

    :attr ifname: the name of the interface
    :attr ip: the interface IPV4
    :attr status: the operational state of the interface
    :param ipdb_interface: a network interface
    :type ipdb_interface: an IPDB interface object
                                <class 'pyroute2.ipdb.interface.Interface'>
    '''
    def __init__(self, ipdb_interface):
        try:
            self.ifname = ipdb_interface.ifname
        except:
            pass
        try:
            self.ip = ipdb_interface.ipaddr[0]['address']
        except:
            pass
        try:
            self.status = ipdb_interface.operstate
        except:
            pass

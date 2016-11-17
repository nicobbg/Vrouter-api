from flask_restplus import Model, fields

model_interface = Model('Interface_model', {
    'ifname': fields.String,
    'ip': fields.String,
    'status': fields.String
})


class InterfaceDao():
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

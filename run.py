# -*- coding: utf8 -*-

from flask import Flask
from apps.apiv1 import blueprint as apiv1

app = Flask(__name__)
app.register_blueprint(apiv1)
app.debug = True

if __name__ == "__main__":
        app.run()

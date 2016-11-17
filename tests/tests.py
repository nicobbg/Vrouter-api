from __future__ import absolute_import
import unittest
import requests
from flask import Flask
from apps.apiv1 import blueprint as apiv1


class TestWSMethods(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(apiv1)

    def test_get_netns(self):
        self.res = requests.get('http://127.0.0.1:5000/api/v1/netnamespaces/')
        self.assertEqual(self.res.status_code, 200)


if __name__ == '__main__':
    unittest.main()

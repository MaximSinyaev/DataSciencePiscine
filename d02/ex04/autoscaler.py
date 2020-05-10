from requests import put
from requests.auth import HTTPBasicAuth

class ClusterManagement:
    def __init__(self, url, name, api_header, login_tuple):
        self.url = url
        self.name = name
        self.http_header = api_header
        self.auth = HTTPBasicAuth(login_tuple)
        self.services = list()

    class ArgError(Exception):
        def __init__(self, message='Not all vars'):
            super().__init__(message)

    def switcher(self, node_name, **kwargs):
        response = put(self.url, headers=self.http_header,
                       data = {}, auth=self.auth)
        for service in kwargs:
            put(self.url, headers=self.http_header,
                           data=service, auth=self.auth)
        return response

    def maintence(self, state, node_name, **kwargs):
        response = put(self.url, headers=self.http_header,
                       data={}, auth=self.auth)
        return response

    def comission(self, state, node_name, **kwargs):
        response = put(self.url, headers=self.http_header,
                       data={}, auth=self.auth)
        return response

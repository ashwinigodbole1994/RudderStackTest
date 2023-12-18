import json
import requests
from common.constant import Constants


class AuthUser(object):

    def login(self, emailId, password):
        POST_AUTH = "/login"
        content_type = 'application/json'
        pydict = json.dumps({"email": emailId, "password": password})
        response = requests.post(Constants.base_url + POST_AUTH, data=pydict, headers={"Content-Type": content_type})
        return response.json()

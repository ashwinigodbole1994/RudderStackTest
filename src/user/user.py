import requests
from common.constant import Constants


class User(object):

    def get_user_info(self, token):
        GET_USER = "/getUser"
        headers = {"content-type": "application/json",
                   "authorization": "Bearer {}".format(token)}
        response = requests.get(Constants.base_url + GET_USER, headers=headers)
        return response.json()

    def get_workspaces_id(self, token):
        GET_USER = "/getUser"
        headers = {"content-type": "application/json",
                   "authorization": "Bearer {}".format(token)}
        response = requests.get(Constants.base_url + GET_USER, headers=headers)
        return response.json()['workspaces'][0]['id']

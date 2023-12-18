import requests
from common.constant import Constants



class Tenant(object):

    def get_tenant_info_using_workspaces_id(self, token, workspaces_id):
        headers = {"content-type": "application/json",
                   "authorization": "Bearer {}".format(token)}
        response = requests.get(Constants.base_url + "/workspaces/" + workspaces_id + "/tenant", headers=headers)
        return response.json()

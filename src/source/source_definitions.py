import requests
from common.constant import Constants


class SourceDefinition(object):

    def get_all_sources_definition(self, token):
        GET_SOURCES = "/web/source-definitions"
        headers = {"content-type": "application/json",
                   "authorization": "Bearer {}".format(token)}
        response = requests.get(Constants.base_url + GET_SOURCES, headers=headers)
        return response.json()
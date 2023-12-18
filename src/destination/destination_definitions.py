import requests
from common.constant import Constants


class DestinationDefinition(object):

    def get_all_destination_definition(self, token):
        GET_DESTINATION = "/web/destination-definitions"
        headers = {"content-type": "application/json",
                   "authorization": "Bearer {}".format(token)}
        response = requests.get(Constants.base_url + GET_DESTINATION, headers=headers)
        return response.json()
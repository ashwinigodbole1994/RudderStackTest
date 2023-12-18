class Helper(object):

    def create_header_request(self, token):
        headers = {"content-type": "application/json",
                   "authorization": "Bearer {}".format(token)}
        return headers
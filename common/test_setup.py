
class SetupTest(object):
    def __init__(self, request=None, username=None, password=None):
        if request is None:
            self.username = username
            self.password = password
            self.test_env_info = None
        else:
            self.username = request.config.getoption("--username", None)
            self.password = request.config.getoption("--password", None)
            self.test_env_info = request.config.getoption("--test_env_info", None)
        self.token = None
        self.cookie = None


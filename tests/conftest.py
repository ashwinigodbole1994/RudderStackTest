import pytest
from common import test_setup
from src.auth.api import AuthUser


def pytest_addoption(parser):
    parser.addoption("--username",
                     action="store",
                     default="coreg11734@astegol.com",
                     help="Username for login")

    parser.addoption("--password",
                     action="store",
                     default="RudderStack@123",
                     help="Password for login")

    parser.addoption("--test_env_info", action="store", help="test environment")


@pytest.fixture(scope="class")
def username(request):
    return request.config.getoption("--username")


@pytest.fixture(scope="class")
def password(request):
    return request.config.getoption("--password")


@pytest.fixture(scope="class")
def setup_test(request):
    auth = AuthUser()
    before_test = test_setup.SetupTest(request)
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    res = auth.login(username, password)
    before_test.token = res['idToken']
    return before_test

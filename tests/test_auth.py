import pytest

from src.auth import api


class TestAuthUser(api.AuthUser):

    def test_auth_user_with_valid_data(self, username, password):
        """
        Steps.
        1. Enter valid emailId and pswd
        2. Try to login with valid data
        3. Check that status code is 200
        4. Check response
        """
        res = self.login(username, password)
        assert res['statusCode'] == 200, "Check status code"
        assert res['status'] == "success", "Verify status"

    def test_auth_user_with_random_data(self, username):
        """
        1. Try to auth user (access to store) with random invalid data
        2. Check that status code is 401
        3. Check response
        """
        res = self.login(username, "temp")
        assert res['message'] == 'Incorrect username or password.', "Check message"

import pytest
from src.user import user


class TestAuthUser(user.User):

    def test_verify_user_info(self, setup_test):
        """
        Steps.
        1. get accesTokn from Login
        2. set that token as b
        3. Check that status code is 200
        4. Check response
        """
        res = self.get_user_info(setup_test.token)
        assert res['email'] == setup_test.username, "verify User name"
        assert res['name'] == "Ashwini", "Verify name of user"
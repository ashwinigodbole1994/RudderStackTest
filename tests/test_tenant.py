from src.tenant import tenant
from src.user.user import User

user_obj = User()


class TestTenant(tenant.Tenant):

    def test_verify_tenant_info_for_workspaces_id(self, setup_test):
        """
        Steps.
        1. get accesTokn from Login
        2. set that token as bearer token
        3. Check that status code is 200
        4. Check response
        """
        workspaces_id = user_obj.get_workspaces_id(setup_test.token)
        res = self.get_tenant_info_using_workspaces_id(setup_test.token, workspaces_id)
        assert res['planName'] == 'Free Tier', "verify Plan name"
        assert res['ownerEmail'] == setup_test.username, "Verify owner email"

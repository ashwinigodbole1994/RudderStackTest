from src.destination import destination_definitions

destination_list = []


class TestDestinationDefinition(destination_definitions.DestinationDefinition):

    def test_verify_all_destination_definition_present_in_system(self, setup_test):
        """
        Steps.
        1. get accesTokn from Login
        2. set that token as bearer token for authorization
        3. hit the Destination-defintion API and Check that status code is 200
        4. Check response
        """
        destinationList = self.get_all_destination_definition(setup_test.token)
        for destination in destinationList:
            destination_list.append(destination['displayName'])
        assert len(destination_list) == 198, "verify count of destination in system"

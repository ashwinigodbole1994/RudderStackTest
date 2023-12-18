from src.source import source_definitions

source_list = []


class TestSourceDefinition(source_definitions.SourceDefinition):

    def test_verify_all_source_definition_present_in_system(self, setup_test):
        """
        Steps.
        1. get accesTokn from Login
        2. set that token as bearer token for authorization
        3. hit the Source-defintion API and Check that status code is 200
        4. Check response
        """
        srcList = self.get_all_sources_definition(setup_test.token)
        for src in srcList:
            source_list.append(src['displayName'])
        assert len(source_list) == 105, "verify count of sources in system"

from unittest import TestCase

import vcr

import lykkex


class TestLykkex(TestCase):
    @vcr.use_cassette('vcr_cassetes/is_alive.yml')
    def test_is_alive_returns_a_dict_with_a_field_for_possible_issues(self):
        response = lykkex.is_alive()
        assert "IssueIndicators" in response.keys()
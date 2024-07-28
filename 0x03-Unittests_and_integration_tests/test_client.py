#!/usr/bin/env python3
"""
    Parameterize and patch decorators
"""
import unittest
from unittest.mock import Mock, patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
        Tests the GithubOrgClient class methods
    """

    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'})
        ])
    @patch('client.get_json')
    def test_org(self, org, response, mock_obj):
        """ Tests the org method """
        mock_obj.return_value = MagicMock(return_value=response)
        githuborgclient = GithubOrgClient(org)
        self.assertEqual(githuborgclient.org(), response)
        mock_obj.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org))

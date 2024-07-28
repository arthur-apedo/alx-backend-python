#!/usr/bin/env python3
"""
    Parameterize and patch decorators
"""
import unittest
from unittest.mock import Mock, patch, MagicMock, PropertyMock
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

    def test_public_repos_url(self):
        """ Tests the _public_repos_url property """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_obj:
            mock_obj.return_value = {
                    'repos_url': 'https://api.github.com/users/google/repos'}
            self.assertEqual(
                    GithubOrgClient('google')._public_repos_url,
                    "https://api.github.com/users/google/repos"
                    )

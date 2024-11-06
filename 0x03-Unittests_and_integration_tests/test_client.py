#!/usr/bin/env python3
"""This module defines a unit test for client.GithubOrgClient."""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient.
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Tests that GithubOrgClient.org returns the correct value.
        """
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """
        Tests that GithubOrgClient._public_repos_url returns the correct value.
        """
        with patch('client.GithubOrgClient.org', new_callable=Mock) as mock_org:
            mock_org.return_value = {"repos_url": "test_url"}
            client = GithubOrgClient("test_org")
            self.assertEqual(client._public_repos_url, "test_url")

    @patch('client.get_json')
    def test_repos_payload(self, mock_get_json):
        """
        Tests that GithubOrgClient.repos_payload returns the correct value.
        """
        with patch('client.GithubOrgClient.org', new_callable=Mock) as mock_org:
            mock_org.return_value = {"repos_url": "test_url"}
            client = GithubOrgClient("test_org")
            client.repos_payload()
            mock_get_json.assert_called_once_with("test_url")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": {}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Tests that GithubOrgClient.has_license returns the correct value.
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected)
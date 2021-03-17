"""
    Author: Jacqueline Ramos
    567 HW05a: This assignment uses 'mocking' to replace the 'request' method from HW04a_Test,
    so as not to depend on calling GitHubAPIs. 
"""

# from unittest.mock import Mock, patch
# from unittest.mock import Mock, patch
import unittest
from unittest import mock
from unittest.mock import patch, Mock
from HW04a_JacquelineRamos import github_repos
import json
import requests


class TestGithubRepos(unittest.TestCase):
    # this class holds the test cases for github_repos

    @mock.patch('requests.get') # patches requests.get so does not call API server

    def test_valid_users(self, mockedRequest):
        # tests a valid github user id
        
        jr_expected = ['Repo: 567HW01 Number of commits 1', 
        'Repo: GitHubAPI567 Number of commits 10', 
        'Repo: hello-world Number of commits 3', 
        'Repo: helloworld Number of commits 1', 
        'Repo: Student-Repository Number of commits 4', 
        'Repo: Triangle567 Number of commits 11']

        mockedRequest.return_value.text = ['Repo: 567HW01 Number of commits 1', 
        'Repo: GitHubAPI567 Number of commits 10', 
        'Repo: hello-world Number of commits 3', 
        'Repo: helloworld Number of commits 1', 
        'Repo: Student-Repository Number of commits 4', 
        'Repo: Triangle567 Number of commits 11']

        result = github_repos('jacquelineramos8')

        self.assertEqual(result, jr_expected)
    
    def test_invalid_users(self, mockedRequest):
        # tests an invalid github user id

        mockedRequest.return_value.text = 'No repositories found'
        result = github_repos('averyfakegithubuserid')
        self.assertEqual(result, 'No repositories found')

if __name__ == '__main__':
    unittest.main()
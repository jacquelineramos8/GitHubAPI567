"""
    Author: Jacqueline Ramos
    567 HW04a Test: This program contains the unittests for the github_repos function,
    which parses JSON files using github API from a github user id input, and returns that user's repos and commits for each repo if present.
"""

import unittest
from HW04a_JacquelineRamos import github_repos

class TestGithubRepos(unittest.TestCase):
    def test_valid_users(self):
        jr_expected = ['Repo: 567HW01 Number of commits 1', 
        'Repo: GitHubAPI567 Number of commits 6', 
        'Repo: hello-world Number of commits 3', 
        'Repo: helloworld Number of commits 1', 
        'Repo: Student-Repository Number of commits 4', 
        'Repo: Triangle567 Number of commits 11']

        self.assertEqual(github_repos('jacquelineramos8'), jr_expected)
    
    def test_invalid_users(self):
        self.assertEqual(github_repos('averyfakegithubuserid'), 'No repositories found')

if __name__ == '__main__':
    unittest.main()

"""
    Author: Jacqueline Ramos
    567 HW04a: This program parses JSON files using github API from a github user id input, 
    and returns that user's repos and commits for each repo (if they exist).
"""

import json
import requests

def github_repos(user_id):
    # this function takes a github user id as input
    # it returns a list of that user's repositories and the number of commits for each repository
    repo_list = []
    url = 'https://api.github.com/users/{}/repos'.format(user_id)
    response = requests.get(url)
    
    github_dict = json.loads(response.text)
    
    for repo in github_dict:
        # this loop parses the repo info and retrieves the name of each repo and the number of commits per repo
        try:
            repo_name = repo["name"]    # if no repo names appear then there are no repos
        except:
            return 'No repositories found'

        repo_url = 'https://api.github.com/repos/{}/{}/commits'.format(user_id, repo_name)
        repo_response = requests.get(repo_url)

        repo_dict = json.loads(repo_response.text)
        repo_list.append('Repo: {} Number of commits {}'.format(repo_name, len(repo_dict)))

    return repo_list


github_repos('jacquelineramos8')




import requests
import json
import sys
import os

class PR(): 
    
    def __init__(self, token, user, repo) -> None:
        self.token = token
        self.user = user
        self.repo = repo
    
    def raise_pr(self, title, head, base):
        url = "https://api.github.com/repos/"+ self.user +"/"+ self.repo+"/pulls"
        payload = json.dumps({
            "title": title,
            "head": head,
            "base": base
        })

        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 201:
            data = response.json()
            return data["number"]
        
        print(response.json())
        return -1
        
    def request_review(self, pr_number, reviewers):
        print("Requesting for reviewers for PR {0}".format(pr_number))
        url = "https://api.github.com/repos/" + self.user + "/" + self.repo + "/pulls/" + str(pr_number) + "/requested_reviewers"
        print(url)
        payload = {
            "reviewers": reviewers
        }
        print(payload)
        headers = {
            'Authorization': 'Bearer ' + self.token
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 201:
            return True
        
        return False

def workflow(token, user, repo, title, head, base, reviewers):
    pr = PR(token, user, repo)

    pr_number = pr.raise_pr(title, head, base)
    if pr_number == -1:
        print("PULL_REQUEST ERROR unable to raise a PR")
    
    review = pr.request_review(pr_number, reviewers)
    if not review:
        print("REVIEW_REQUEST ERROR unable to add reviewer to the PR")

if __name__ == '__main__':
    if len(sys.argv) < 8:
        print("Usage: python3 main.py <token> <user> <repo> <pull request title> <pull request head> <pull request base> <pull request reviewers>")
        sys.exit(1)
    
    workflow(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7].split(","))

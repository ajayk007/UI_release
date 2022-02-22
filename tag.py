import requests
import json
import sys
import os
class PR():
    def __init__(self, token, user, repo) -> None:
        self.token = token
        self.user = user
        self.repo = repo

    def generate_release_notes(self, tag):
        url = "https://api.github.com/repos/"+ self.user +"/"+ self.repo+"/releases/generate-notes"
        payload = json.dumps({
            "tag_name": tag
        })

        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            return response.json()
        
        return {
            "name": tag,
            "body": "## What's Changed\n**Full Changelog**: https://github.com/amagimedia/bifrost/commits/" + tag
        }
    
    def create_release(self, tag):
        resp = self.generate_release_notes(tag)

        url = "https://api.github.com/repos/"+ self.user +"/"+ self.repo+"/releases"
        payload = json.dumps({
            "tag_name": tag,
            "name": resp["name"],
            "body": resp["body"]
        })

        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

def workflow(token, user, repo, tag):
    pr = PR(token, user, repo)
    pr.create_release(tag)
    
if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Usage: python3 main.py <token> <user> <repo> <tag>")
        sys.exit(1)
    
    workflow(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

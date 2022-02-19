import argparse
import yaml
import json

class Manager():
    def __init__(self, branch) -> None:
        self.branch = branch
    
    def increment_version(self, version):
        with open("../" + self.branch + "/release.json") as json_file:
            release = json.load(json_file)
        version = version.split('.')
        version[2] = str(int(version[2]) + 1)
        return '.'.join(version)

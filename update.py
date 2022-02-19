
import yaml
import json

class Manager():
    
    def __init__(self) -> None
  
    
    def process(self):
        with open("../" + "release.json") as json_file:
            release = json.load(json_file)
        release["last_version"] = release["next_version"]
        release["next_version"] = self.increment_version(release["next_version"])
    
    def increment_version(self, version):
        version = version.split('.')
        version[2] = str(int(version[2]) + 1)
        return '.'.join(version)
if __name__ == '__main__':
    m = Manager()
    m.process()

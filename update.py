
import yaml
import json

class Manager():
    
    def __init__(self) -> None:
        print("nothing here")
    
    def process(self):
        with open("../" + "UI_release" +"/UI_release.json") as json_file:
            release = json.load(json_file)
        release["last_version"] = release["next_version"]
        release["next_version"] = self.increment_version(release["next_version"])
        with open("../" + "UI_release" + "/UI_release.json", 'w') as outfile:
            json.dump(release, outfile, indent=2)
    
    def increment_version(self, version):
        version = version.split('.')
        version[1] = str(int(version[1]) + 1)
        return '.'.join(version)

if __name__ == '__main__':
    m = Manager()
    m.process()

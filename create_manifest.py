import json
import os
from icecream import ic


# Read the .curseclient file
def read_project_guid():
    with open(".curseclient", "r") as f:
        return f.readline().strip()


# Read the "%APPDATA%\\Local\\Overwolf\\Curse\\GameInstances\\MinecraftGameInstance.json file for the project info.
def read_all_curseforge_data():
    # Find the AppData folder
    appdata = os.getenv("APPDATA")

    print(appdata)

    # Get out of the Roaming folder
    appdata = os.path.dirname(appdata)

    print(appdata)

    # Find the Curse folder
    curse_folder = os.path.join(appdata, "Local", "Overwolf", "Curse", "GameInstances")

    print(curse_folder)
    # Join the Curse folder with the MinecraftGameInstance.json file
    game_instance = os.path.join(curse_folder, "MinecraftGameInstance.json")

    print(game_instance)

    # Read the MinecraftGameInstance.json file
    with open(game_instance, "r", encoding="UTF-8") as f:
        project_data = f.readline()

        # Parse the JSON
        project_data = json.loads(project_data)

        return project_data


project_guid = read_project_guid()
print(project_guid)

data = read_all_curseforge_data()


def find_project(guid):
    for project in data:
        if project["guid"] == guid:
            return project

    return None


def list_mod_ids(project):
    addon_ids = []
    for addon in project["installedAddons"]:
        addon_ids.append(addon["addonID"])

    return addon_ids


project_data = ic(find_project(project_guid))

# Get the installed addons
mod_ids = list_mod_ids(project_data)

print(mod_ids)

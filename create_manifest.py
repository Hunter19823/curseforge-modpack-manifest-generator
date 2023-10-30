import json
import os
from icecream import ic

import generate


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


def find_project(guid):
    for project_data in curseforge_data:
        if project_data["guid"] == guid:
            return project_data

    return None


def list_file_data(project_data):
    file_data = []
    for addon in project_data["installedAddons"]:
        file_data.append({
            "projectID": addon["addonId"],
            "fileID": addon["id"],
            "required": True
        })

    return file_data


def save_modlist(addon_ids):
    with open("mods.txt", "w") as f:
        for addon_id in addon_ids:
            f.write(str(addon_id) + "\n")


def read_manifest_template():
    # Reads manifest template
    with open('manifest-template.json') as m:
        manifest = json.load(m)
        return manifest


if __name__ == "__main__":
    project_guid = read_project_guid()

    curseforge_data = read_all_curseforge_data()

    project = ic(find_project(project_guid))

    template = read_manifest_template()

    # Get the installed addons
    template["files"] = list_file_data(project)
    template["minecraft"]["version"] = project["baseModLoader"]["minecraftVersion"]
    template["minecraft"]["modLoaders"] = []
    template["minecraft"]["modLoaders"].append({
        "id": project["baseModLoader"]["name"],
        "primary": True
    })



    # Create a mods.txt file with all the mod IDs
    save_modlist(mod_ids)

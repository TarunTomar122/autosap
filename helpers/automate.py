import os

def show_dir_list(dir_name):
    folders = []
    for folder in os.listdir(dir_name):
        if os.path.isdir(os.path.join(dir_name, folder)):
            folders.append(folder)
    return folders


def show_files_in_dir(dir_name):
    files = []
    for file in os.listdir(dir_name):
        if os.path.isfile(os.path.join(dir_name, file)):
            files.append(file)
    return files


class Automate:

    project_folder = "F:/0.CurrProjects"

    def get_projects(self):

        projects = show_dir_list(self.project_folder)

        return projects

    def open_folder(self, folder_name):

        folder_path = self.project_folder + "/" + folder_name

        folders = show_dir_list(folder_path)

        files = show_files_in_dir(folder_path)

        return folders, files

    def get_file_content(self, file_name):

        file_path = self.project_folder + "/" + file_name

        with open(file_path, 'r') as file:
            content = file.read()

        return content

    def start_setup(self, prefix):

        path = self.project_folder + "/" + prefix

        files = show_files_in_dir(path)

        if 'App.js' in files:

            os.system("code " + path)

            run_command = "start \"\" cmd /k \"cd /D " + path + " && npm start\""
            os.system(run_command)

            open_emulator_command = "start \"\" cmd /k \"cd /D C:/Users/tomar/AppData/Local/Android/sdk/emulator && emulator -avd Two_D\""
            os.system(open_emulator_command)

        elif 'index.js' in files:

            os.system("code " + path)

            run_command = "start \"\" cmd /k \"cd /D " + path + " && npm start\""
            os.system(run_command)

        else:

            os.system("code " + path)

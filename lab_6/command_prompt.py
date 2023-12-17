import os
from lab_6.decorator import method_decorator

<<<<<<< HEAD
=======

>>>>>>> origin/main
class CommandPrompt():
    def __init__(self):
        self.path = os.getcwd()
        print(f'Current directory: {self.path}')

    @method_decorator
    def directory(self):
        try:
            print('Contains:')
            for item in os.listdir(self.path):
                print(item)
        except FileNotFoundError:
            print("Incorrect path")

    @method_decorator
    def change_directory(self, path):
        try:
            if path == '..':
                os.chdir(path)
            else:
                self.path = f'{self.path}/{path}'
                os.chdir(self.path)
            self.path = os.getcwd()
            print(f'Current directory: {self.path}')
        except FileNotFoundError:
            print("Incorrect path")

    @method_decorator
    def create_folder(self, name):
        try:
            full_path = os.path.join(self.path, name)
            os.mkdir(full_path)
        except FileExistsError:
            print(f'Folder {name} is exists')
        except FileNotFoundError:
            print("Incorrect path")

    @method_decorator
    def delete_folder(self,name):
        try:
            os.rmdir(name)
        except FileNotFoundError:
            print(f"Folder {name} is not found")

    @method_decorator
    def create_file(self,name):
        try:
            with open(name, 'x'):
                pass
        except FileExistsError:
            print(f'File {name} exists')

    @method_decorator
    def view_file(self,name):
        try:
            with open(name, 'r') as file:
                for item in file.readlines():
                    print(item)
        except FileNotFoundError:
            print(f"File {name} is not found")

    @method_decorator
    def rename(self,old_name, new_name):
        try:
            os.rename(old_name, new_name)
        except FileNotFoundError:
            print(f"File of folder {old_name} is not found")

    @method_decorator
    def delete_file(self,name):
        try:
            os.remove(name)
        except FileNotFoundError:
            print(f"File {name} is not found")

    def read_command(self, cmd):
        list_cmd = cmd.split(' ')
        command = list_cmd[0]
        agr1 = ''
        agr2 = ''

        if len(list_cmd) == 2:
            agr1 = list_cmd[1]
        if len(list_cmd) == 3:
            agr2 = list_cmd[2]

        return command, agr1, agr2

    @method_decorator
    def help(sefl):
        print("""
        1. dir - shows list of files in directory
        2. cd - change directory with argument [path] - path to move, [..] - go to up by directory, 
        3. mkdir - create folder in current directory
        4. rmdir - remove folder in current directory with argument [name of folder]
        5. mkfile - create file in current directory with argument [name of file]
        6. rmfile - delete file in current directory with argument [name of file]
        7. open - view file in current directory with argument [name of file]
        8. rename -  rename file/folder in current directory with argument [name of file/folder]""")

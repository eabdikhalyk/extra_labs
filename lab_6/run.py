from command_prompt import CommandPrompt

print('You ran CMD. If you would like know about commands type "help".')
cmd = CommandPrompt()
is_go_on = True

while is_go_on:
    text = input("")
    command, arg1, arg2 = cmd.read_command(text)
    match command:
        case 'dir':
            cmd.directory()
        case 'cd':
            cmd.change_directory(path= arg1)
        case 'mkdir':
            cmd.create_folder(name= arg1)
        case 'rmdir':
            cmd.delete_folder(name=arg1)
        case 'mkfile':
            cmd.create_file(name=arg1)
        case 'rmfile':
            cmd.delete_file(name=arg1)
        case 'open':
             cmd.view_file(name=arg1)
        case 'rename':
            cmd.rename(old_name=arg1,new_name=arg2)
        case 'help':
            cmd.help()
        case 'exit':
            is_go_on = False
        case _:
            print("Incorrect command")
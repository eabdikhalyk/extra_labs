user_list = []
is_go_on = True
is_unique = True
auth = 'Authorization'
option = f'''Choose one option:
1. Create User
2. Show list of Users
3. Delete user from list
4. Authorization
5. Exit
'''
def password_validation():
    while True:
        password = input("Password: ")
        if len(password) >= 8:
            return password
        else:
            print("Password should equal or longer than 8 characters")
def email_validation():
    global is_unique
    while True:
        email = input("Email: ")
        is_unique = True
        for i in  range(0, len(user_list)):
            if user_list[i]['Email'] == email:
                print(f"{email} exists, it should be unique")
                is_unique = False
        if is_unique:
            return email


def create_user():
    name = input("Name: ")
    surname = input("Surname: ")
    age = input("Age: ")
    address = input('Address: ')
    email = email_validation()
    password = password_validation()
    user={
        'Name':name,
        'Surname': surname,
        'Age': age,
        'Address': address,
        'Email': email,
        'Password': password,
    }
    user_list.append(user)
    print("User created.")

def show_user_list():
    if user_list:
        for user in user_list:
            print(f"Name: {user['Name']}, Surname: {user['Surname']}, "
                  f"Age: {user['Age']}, Address: {user['Address']}, Email: {user['Email']}")
    else:
        print('list of Users is empty.')

def delete_user():
    email = input("Enter email of user who you want delete: ")
    is_deletion = True
    if user_list:
        for i in range(0, len(user_list)-1):
            if user_list[i]['Email'] == email:
                user_list.pop(i)
                print(f"User with {email} was deleted.")
                is_deletion = False
        if is_deletion:
            print(f"User with {email} does not exist.")
    else:
        print('list of Users is empty.')
def authorization():
    if user_list:
        for _ in range(0,3):
            email = input('Enter email: ')
            password = input('Enter password: ')
            for item in user_list:
                global auth
                if item['Email'] == email and item['Password'] == password:
                    print(f'You are successfully logged in to the system.')
                    print(f"Hello, {item['Name']}!")
                    option.replace("Authorization","Logout")
                    auth = 'Logout'
                    return
            print("Wrong email or password")
    else:
        print('list of Users is empty.')

def logout():
    global auth
    print("You are successfully logged out ")
    option.replace("Logout", "Authorization")
    auth = "Authorization"
def exit():
    global is_go_on
    print("Good bye!")
    is_go_on = False


while is_go_on:
    print(option)
    choice = input("")
    if choice == '1':
        create_user()
    elif choice == '2':
        show_user_list()
    elif choice == '3':
        delete_user()
    elif choice == '4':
        if auth == 'Authorization':
            authorization()
        else:
            logout()
    elif choice == '5':
        exit()
    print('\n')

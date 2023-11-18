
options='''Available options:
1. a + b
2. a - b
3. a * b
4. a % b
5. Fibonacci number
6. Exit
'''
a = 0.0
b = 0.0
is_go_on = True

def print_options():
    print(options)

def input_operators():
    global a,b
    is_string = True
    while is_string:
        try:
            a = float(input("insert a: "))
            b = float(input("insert b: "))
            is_string = False
        except:
            print("You entered string, please enter number")

def add():
    print("1. a + b")
    input_operators()
    result = a + b
    print(f"Answer a + b = {result}")

def subtract():
    print("2. a - b")
    input_operators()
    result = a - b
    print(f"Answer a - b = {result}")

def multiply():
    print("3. a * b")
    input_operators()
    result = a * b
    print(f"Answer a * b = {result}")

def divide():
    print("4. a % b")
    input_operators()
    try:
        result = a / b
        print(f"Answer a % b = {result}")
    except ZeroDivisionError:
        print("Zero Division Error")

def fibonacci():
    print("5. Fibonacci number")
    fnum1 = 1
    fnum2 = 1
    i = 0
    n = int(input("Enter the number of the Fibonacci number: "))
    while i < n -2:
        fnumSum = fnum1 + fnum2
        fnum1 = fnum2
        fnum2 = fnumSum
        i+=1

    print(f"Answer: {fnum2}")

while is_go_on:
    print_options()
    chosen_option = int(input('Enter option: '))
    if chosen_option == 1:
        add()
    elif chosen_option == 2:
        subtract()
    elif chosen_option == 3:
        multiply()
    elif chosen_option == 4:
        divide()
    elif chosen_option == 5:
        fibonacci()
    elif chosen_option == 6:
        print("Good bye!")
        is_go_on = False

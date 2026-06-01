# import personpackage
# from personpackage import get_statement
from personpackage import get_statement as statement

while input("Press x to eXit : ").lower() != "x":
    try:
        user = {}
        user["name"] = input("Please tell me your name : ")
        user["age"] = int(input("Please tell me your age : "))
        message = statement(user)
        with open('user_info.txt', 'a') as write_user:
            write_user.write(f'{message}\n')
        print(message)
    except ValueError as val_err:
        print(f'Age must be a number.')

with open('user_info.txt', 'r') as read_user:
    for user in read_user.readlines():
        print(user)
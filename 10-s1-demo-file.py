def get_age_status(age):
    if age < 12:
        return 'a child'
    elif age < 18:
        return 'a teenager'
    elif age < 25:
        return 'a young adult'
    elif age < 60:
        return 'an adult'
    elif age < 100:
        return 'a senior'
    else:
        return 'a centenarian'

def get_statement(user):
    return f'Hi {user["name"]}, you are {get_age_status(user["age"])}'

while input("Press x to eXit : ").lower() != "x":
    try:
        user = {}
        user["name"] = input("Please tell me your name : ")
        user["age"] = int(input("Please tell me your age : "))
        message = get_statement(user)
        with open('user_info.txt', 'a') as write_user:
            write_user.write(f'{message}\n')
        print(message)
    except ValueError as val_err:
        print(f'Age must be a number.')

with open('user_info.txt', 'r') as read_user:
    for user in read_user.readlines():
        print(user)
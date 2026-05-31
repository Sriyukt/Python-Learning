user_list = []

def get_age_status(age):
    if age < 12:
        return f'You are a child'
    elif age < 18:
        return f'You are a teenager'
    elif age < 25:
        return f'You are a young adult'
    elif age < 60:
        return f'You are an adult'
    elif age < 100:
        return f'You are a senior citizen'
    else:
        return f'You are a centenarian'

def get_statement(user):
    return f'Hi! {user["name"]}, {get_age_status(user["age"])}.'

while input("Press x to eXit : ").lower() != 'x':
    user = {}
    user["name"] = input("Please tell me your name : ")
    try:
        user["age"] = int(input("Please tell me your age : "))
        print(get_statement(user))
        user_list.append(user)
    except ValueError as val_err:
        print(f'Age has to be a number. {val_err}')

for user in user_list:
    print(get_statement(user))

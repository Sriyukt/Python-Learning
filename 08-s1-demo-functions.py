user_list = []
scope = "I am in global scope"

def get_age_status(age):
    print(scope)
    # scope = "I am in get_age_status function"
    # print(scope)
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
    print(scope)
    # scope = "I am in get_statement function"
    # print(scope)
    return f'Hi! {user["name"]}, {get_age_status(user["age"])}.'

while input("Press x to eXit : ").lower() != 'x':
    user = {}
    print(scope)
    user["name"] = input("Please tell me your name : ")
    user["age"] = int(input("Please tell me your age : "))

    print(get_statement(user))
    print(scope)
    user_list.append(user)

for user in user_list:
    print(get_statement(user))
    print(scope)

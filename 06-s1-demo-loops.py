
while input("Press x to eXit : ").lower() != 'x':
    user = {}

    user["name"] = input("Please tell me your name : ")
    user["age"] = int(input("Please tell me your age : "))

    print(f'Hi, {user["name"]}')

    if user["age"] < 12:
        print(f'You are a child')
    elif user["age"] < 18:
        print(f'You are a teenager')
    elif user["age"] < 25:
        print(f'You are a young adult')
    elif user["age"] < 60:
        print(f'You are an adult')
    elif user["age"] < 100:
        print(f'You are a senior citizen')
    else:
        print(f'You are a centenarian')
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
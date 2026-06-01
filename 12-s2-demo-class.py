from personclass import person

while input("Press x to eXit : ").lower() != 'x':
    try:
        user_name = input("Please tell me your name : ")
        user_age = int(input("Please tell me your age : "))
        user = person(user_name,user_age)
        message = user.get_statement()         
        print(message)
        with open("./user_info.txt","a") as user_adder:
            user_adder.write(message+'\n')
    except ValueError as val_err:
        print(f'Age has to be a number.')

with open("./user_info.txt","r") as user_fetcher:
    for line in user_fetcher.readlines():
        print(line)
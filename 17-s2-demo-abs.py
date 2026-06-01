from countryabs import national, being

while input("Press x to eXit : ").lower() != 'x':
    try:
        # user_test = being()
        user_name = input("Please tell me your name : ")
        user_age = int(input("Please tell me your age : "))
        user_country = input("Please tell me the name of country you live in : ")
        user = national(user_name,user_age,user_country)
        message = user.get_statement()
        # message = user.get_statements()
        print(message)
        with open("./user_info.txt","a") as user_adder:
            user_adder.write(message+'\n')
    except ValueError as val_err:
        print(f'Age has to be a number.')

with open("./user_info.txt","r") as user_fetcher:
    for line in user_fetcher.readlines():
        print(line)
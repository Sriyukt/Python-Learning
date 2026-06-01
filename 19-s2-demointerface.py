from requests import get, post

while input("Press x to eXit : ").lower() != 'x':
    try:
        user_name = input("Please tell me your name : ")
        user_age = int(input("Please tell me your age : "))
        user_country = input("Please tell me the name of country you live in : ")
        req = {"name":user_name,"age":user_age,"country":user_country}
        check = get("http://127.0.0.1:5000/status").json()
        if check["status"]=="success":
            res = post(url="http://127.0.0.1:5000/status",data=req).json()
            with open("./user_info.txt", "a") as recorduser:
                recorduser.write(res["message"]+"\n")
                print(res["message"])
        else:
            print(check["message"])
    except Exception as err:
        print(f'ERROR : {err}')

with open("./user_info.txt","r") as user_fetcher:
    for line in user_fetcher.readlines():
        print(line)
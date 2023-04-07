import re
name =input("please enter your name : ")
if not name.strip().isalpha():
    print("invalid input")
    exit()
else:
    email =input("please enter your email : ") 
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if not name.strip():
        print("invalid email")
        exit()
    elif not re.fullmatch(regex, email):
        print("invalid email format ")
        exit()
    else:
        print(name)
        print(email)
       
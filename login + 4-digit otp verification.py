import random
userid = input("enter user id: ")
password = input("enter password: ")

if userid =="admin" and password == "1234":
    otp = random.randint(1000,9999)
    print("OTP:", otp)

    user_otp = int(input("enter otp: "))

    if user_otp ==otp:
        print("login succesful")
    else:
        print("invalid otp")
else:
    print("invalid user id or password")


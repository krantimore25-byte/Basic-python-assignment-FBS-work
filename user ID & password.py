uid = "admin"
pwd = "1234"
for i in range(3):
    user = input("Enter user ID: ")
    password = input("Enter password: ")

    if user == uid and password == pwd:
        print("Login successful")
        break
    else:
        print("Invalid credentials")
else:
    print("Program terminated")
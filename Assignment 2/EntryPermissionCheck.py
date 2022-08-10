username = "amir"
password = 1378
loginUsername = input("Enter your username : ")
loginPassword = int(input("Enter your password : "))
numberOfTry = 2
if username != loginUsername or password != loginPassword:
    while (username != loginUsername or password != loginPassword) and numberOfTry != 0:
        loginUsername = input("Enter your username : ")
        loginPassword = int(input("Enter your password : "))
        numberOfTry -= 1
    print("You can't login.")
else:
    print("Wellcome.")
password = 1234
reportThePolice = 4321
numberOfAttempts = 3
while numberOfAttempts > 0:
    userPassword = int(input("Enter the password: "))
    if userPassword // 10000 != 0 or userPassword <= 999:
        continue
    elif userPassword == password:
        print("Entered.")
        break
    elif userPassword == reportThePolice:
        print("Is the card yours!!!?\nIt was reported to the police.")
        break
    else:
        print("The password is wrong!")
        numberOfAttempts -= 1
if numberOfAttempts == 0:
    print("The account was locked.")

number = int(input("Enter the number: "))
if number % 7 ==0:
    print("It's a multiple of 7.")
else:
    while number % 7 != 0:
        number +=1
    print(f'Next multiple of 7 = {number}')

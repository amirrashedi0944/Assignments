number = int(input("Enter the number: "))
inverse = 0
temp = number
while temp != 0:
    inverse = (10 * inverse) + (temp % 10)
    temp = temp // 10
print(f'number = {number}\nThe inverse of the number = {inverse}')
if number == inverse:
    print("The number is equal to it's inverse")
else:
    print("The number is not equal to it's inverse")

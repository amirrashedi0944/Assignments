number = int(input("Enter a six-digit number : "))
temp = number // 10
second = temp % 10
temp = number // 10000
fifth = temp % 10
sum = second + fifth
print(f'The sum of second and fifth digits of the number = {sum} ')

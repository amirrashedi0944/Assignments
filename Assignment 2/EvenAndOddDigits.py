number = int(input("Enter the number : "))
odd = 0
even = 0
while number != 0:
    mod = number % 10
    if mod % 2 == 0:
        even += 1
    else:
        odd += 1
    number = number // 10
print(f'The number of even digits = {even}')
print(f'The number of odd digits = {odd}')
if odd == even:
    print("The number of odd digits is equal to the number of even digits")
elif odd > even:
    print(f'The number of odd digits is {odd - even} more than even digits.')
else:
    print(f'The number of even digits is {even - odd} more than odd digits.')

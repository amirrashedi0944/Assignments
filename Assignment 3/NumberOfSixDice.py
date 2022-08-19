import random as rnd
sumOfNumbers = 0
counter = 1
while True:
    number = rnd.randint(1, 6)
    sumOfNumbers += number
    print(f'{counter:<1} throw of the dice: {number:>2}')
    counter += 1
    if number == 6:
        break
print(f'Sum of numbers equals to {sumOfNumbers}.')


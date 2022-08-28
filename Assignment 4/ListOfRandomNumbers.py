import random
counter = 1
random_numbers = []
length = int(input("""Enter the length of list.
Between one and ten thousand.
>>> """))
if length <= 0 or length > 10_000:
    print("Length must be between one and ten thousand.")
else:
    while counter <= length:
        number = random.randint(1, 10_000)
        if number in random_numbers:
            counter -= 1
        else:
            random_numbers.append(number)
        counter += 1
    print(random_numbers)

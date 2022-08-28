user_numbers = []
sorted_list = []
for i in range(1, 11):
    number = float(input(f"{i:>2}. Enter the number: "))
    if number % 1 == 0:
        number = int(number)
    user_numbers.append(number)
print(f'Your list:\n{user_numbers}')
for i in range(len(user_numbers)):
    number = min(user_numbers)
    sorted_list.append(number)
    user_numbers.remove(number)
print(f'Sorted list:\n{sorted_list}')

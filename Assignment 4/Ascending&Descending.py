numbers_list = []
flag = True
for i in range(1, 11):
    number = float(input(f"{i:>2} Enter the number : "))
    if number % 1 == 0:
        number = int(number)
    numbers_list.append(number)
print(numbers_list)
sorted_list = sorted(numbers_list)
reverse_sorted_list = sorted(numbers_list, reverse=True)
while True:
    for item in numbers_list:
        count = numbers_list.count(item)
        if count != 1:
            flag = False
            break
    break
if numbers_list == sorted_list and flag:
    flag = True
if numbers_list == reverse_sorted_list and flag:
    flag = True
if flag:
    print("Yes.")
else:
    print("NO.")

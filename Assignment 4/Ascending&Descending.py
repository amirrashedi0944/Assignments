numbers_list = []
flag = True
for i in range(1, 11):
    number = float(input(f"{i:>2} Enter the number : "))
    if number % 1 == 0:
        number = int(number)
    numbers_list.append(number)
temp_list = numbers_list[:]
sorted_list = []
reverse_sorted_list = []
for j in range(len(numbers_list)):
    number = min(temp_list)
    sorted_list.append(number)
    temp_list.remove(number)
temp_list = numbers_list[:]
for j in range(len(numbers_list)):
    number = max(temp_list)
    reverse_sorted_list.append(number)
    temp_list.remove(number)
print(numbers_list)
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

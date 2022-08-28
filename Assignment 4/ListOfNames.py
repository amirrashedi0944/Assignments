names_list = []

number = int(input("Enter the number of names you want to add to the list: "))
for i in range(1, number+1):
    name = input(f"{i:>2}. Enter the name: ")
    names_list.append(name)
print(names_list)
names_set = []
for name in names_list:
    if name in names_set:
        continue
    else:
        names_set.append(name)
for name in names_set:
    counter = 0
    for item in names_list:
        if name == item:
            counter += 1
    print(f'{counter}\t{name}')

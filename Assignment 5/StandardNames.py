names = []
for i in range(1, 11):
    name = input(f"{i}. Enter the name: ")
    names.append(name)

standard_names = []
for name in names:
    name = name.title()
    standard_names.append(name)
print(standard_names)

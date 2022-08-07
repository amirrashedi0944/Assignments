radius = float(input("Enter the radius of cylinder : "))
height = float(input("Enter the height of cylinder : "))
pi = 3.14
volume = ((pi * height) * radius ** 2)
lateralArea = (2 * pi * radius * height)
totalArea = ((2 * pi) * radius ** 2) + lateralArea
print(f'The volume of the cylinder is equal to {volume:.2f} .')
print(f'The lateral area of the cylinder is equal to {lateralArea:.2f} .')
print(f'The total area of the cylinder is equal to {totalArea:.2f} .')

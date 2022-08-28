bakery_queue = ["Ali", "Atefe", "Reza", "Homa", "Amir", "Fatemeh"]
print("The queue is like this")
for person in bakery_queue:
    print(person, end="\t")
print()
counter = 1
while counter <= 3:
    name = input("Enter the name: ")
    position = int(input(f"""Enter the place in the queue.
    from 1 to {len(bakery_queue)+1}: """))
    if 1 <= position <= len(bakery_queue)+1:
        bakery_queue.insert(position-1, name)
        counter += 1
    else:
        print(f'The position in the queue must be between 1 and {len(bakery_queue)+1}')
        continue
print("The queue is like this at the end.")
for person in bakery_queue:
    print(person, end="\t")

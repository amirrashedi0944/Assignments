height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bodyMassIndex = round(weight / (height ** 2), 2)
print(f'Body mass index = {bodyMassIndex}')
if bodyMassIndex <= 16:
    print("You have severe underweight, need to think seriously.")
elif 16 < bodyMassIndex <= 18.5:
    print("You are underweight, pay more attention.")
elif 18.5 < bodyMassIndex <= 24:
    print("BMI is suitable, keep it constant.")
elif 24 < bodyMassIndex <= 30:
    print("You are a little overweight.")
elif 30 < bodyMassIndex <= 35:
    print("You have first degree obesity, try to reach ideal wight.")
elif 35 < bodyMassIndex <= 40:
    print("You have second degree obesity, try harder to reach ideal wight.")
else:
    print("You have third degree obesity, need to think seriously.")

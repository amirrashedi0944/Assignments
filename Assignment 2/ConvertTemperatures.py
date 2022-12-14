selection = input("""Select one:
1.Celsius to Fahrenheit
2.Celsius to Kelvin
3.Fahrenheit to Celsius
4.Fahrenheit to Kelvin
5.Kelvin to Celsius
6.Kelvin to Fahrenheit
Choose which one from 1 to 6: """)
if selection == "1":
    temperature = float(input("Enter the temperature in Celsius: "))
    result = (temperature * 1.8) + 32
    result = '{} degrees Celsius equals {:.2f} degrees Fahrenheit.'.format(temperature, result)
elif selection == "2":
    temperature = float(input("Enter the temperature in Celsius: "))
    result = temperature + 273.15
    result = '{} degrees Celsius equals {:.2f} degrees Kelvin.'.format(temperature, result)
elif selection == "3":
    temperature = float(input("Enter the temperature in Fahrenheit: "))
    result = (temperature - 32) * 5 / 9
    result = '{} degrees Fahrenheit equals {:.2f} degrees Celsius.'.format(temperature, result)
elif selection == "4":
    temperature = float(input("Enter the temperature in Fahrenheit: "))
    result = ((temperature - 32) * 5 / 9) + 273.15
    result = '{} degrees Fahrenheit equals {:.2f} degrees Kelvin.'.format(temperature, result)
elif selection == "5":
    temperature = float(input("Enter the temperature in Kelvin: "))
    result = temperature - 273.15
    result = '{} degrees Kelvin equals {:.2f} degrees Celsius.'.format(temperature, result)
elif selection == "6":
    temperature = float(input("Enter the temperature in Kelvin: "))
    result = ((temperature - 273.15) * 1.8) + 32
    result = '{} degrees Kelvin equals {:.2f} degrees Fahrenheit'.format(temperature, result)
else:
    result = "Invalid input.\nChoose from options 1 to 6"
print(result)

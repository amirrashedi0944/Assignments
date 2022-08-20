import mpmath
import statistics
while True:
    selection = input("""
Select what you want:
1.Basic
2.Trigonometric ratios
3.Statistics
4.Exit
>>>>""")
    #Start basic
    if selection == "1" or selection == "Basic" or selection == "basic":
        computingAction =input("""\t\tChoose mathematical computing action:
        1.Addition
        2.Subtraction
        3.Multiplication
        4.Division(Correct division)
        5.Remainder
        6.Number to the power of 2
        7.Number to the power of number
        8.Radical from a number
        9.Back
         >>>>""")
        if computingAction == "1" or computingAction == "Addition" or computingAction == "addition":
            firstNumber = float(input("Enter the first number: "))
            secondNumber = float(input("Enter the second number: "))
            if firstNumber % 1 == 0 and secondNumber % 1 == 0:
                firstNumber = int(firstNumber)
                secondNumber = int(secondNumber)
            result = '{} + {} = {}'.format(firstNumber, secondNumber, firstNumber + secondNumber)
        elif computingAction == "2" or computingAction == "Subtraction" or computingAction == "subtraction":
            firstNumber = float(input("Enter the first number: "))
            secondNumber = float(input("Enter the second number: "))
            if firstNumber % 1 == 0 and secondNumber % 1 == 0:
                firstNumber = int(firstNumber)
                secondNumber = int(secondNumber)
            result = '{} - {} = {}'.format(firstNumber, secondNumber, firstNumber - secondNumber)
        elif computingAction == "3" or computingAction == "Multiplication" or computingAction == "multiplication":
            firstNumber = float(input("Enter the first number: "))
            secondNumber = float(input("Enter the second number: "))
            if firstNumber % 1 == 0 and secondNumber % 1 == 0:
                firstNumber = int(firstNumber)
                secondNumber = int(secondNumber)
            result = '{} * {} = {}'.format(firstNumber, secondNumber, firstNumber * secondNumber)
        elif computingAction == "4" or computingAction == "Division" or computingAction == "division":
            firstNumber = float(input("Enter the first number: "))
            secondNumber = float(input("Enter the second number: "))
            if firstNumber % 1 == 0 and secondNumber % 1 == 0:
                firstNumber = int(firstNumber)
                secondNumber = int(secondNumber)
            result = '{} // {} = {}'.format(firstNumber, secondNumber, firstNumber // secondNumber)
        elif computingAction == "5" or computingAction == "Remainder" or computingAction == "remainder":
            firstNumber = float(input("Enter the first number: "))
            secondNumber = float(input("Enter the second number: "))
            if firstNumber % 1 == 0 and secondNumber % 1 == 0:
                firstNumber = int(firstNumber)
                secondNumber = int(secondNumber)
            result = '{} % {} = {}'.format(firstNumber, secondNumber, firstNumber % secondNumber)
        elif computingAction == "6" or computingAction == "Power 2" or computingAction == "power 2":
            number = float(input("Enter the number: "))
            result = 'The second power of {} is {}'.format(number, number ** 2)
        elif computingAction == "7":
            number = float(input("Enter the number: "))
            power = float(input("Enter the power: "))
            result = '{} to the power of {} is {}'.format(number, power, number ** power)
        elif computingAction == "8" or computingAction == "Radical" or computingAction == "radical":
            number = float(input("Enter the number:"))
            result = 'The square root of {} is equal to {}'.format(number, mpmath.sqrt(number))
        elif computingAction == "9" or computingAction == "Back" or computingAction == "back":
            continue
        else:
            result = "Choose from the options."
        print(result)
    #__________________________________________________________
    #End basic
    #Start trigonometric ratios
    elif selection == "2" or selection == "Trigonometric ratios":
        pi = mpmath.pi
        computingAction = input("""\t\tChoose mathematical computing action:
        1.Sin
        2.Cos
        3.Tan
        4.Cot
        5.Convert degrees to radians
        6.Convert radians to degrees
        7.Back
        >>>""")
        if computingAction == "1" or computingAction == "Sin" or computingAction == "sin":
            angle = float(input("Enter the angle in degrees: "))
            temp = angle
            angle = (angle * pi) / 180
            result = 'Sin{} equals to {}.'.format(temp, mpmath.sin(angle))
        elif computingAction == "2" or computingAction == "Cos" or computingAction == "cos":
            angle = float(input("Enter the angle in degrees: "))
            temp = angle
            angle = (angle * pi) / 180
            result = 'Cos{} equals to {}.'.format(temp, mpmath.cos(angle))
        elif computingAction == "3" or computingAction == "Tan" or computingAction == "tan":
            angle = float(input("Enter the angle in degrees: "))
            temp = angle
            angle = (angle * pi) / 180
            result = 'Tan{} equals to {}.'.format(temp, mpmath.tan(angle))
        elif computingAction == "4" or computingAction == "Cot" or computingAction == "cot":
            angle = float(input("Enter the angle in degrees: "))
            temp = angle
            angle = (angle * pi) / 180
            result = 'Cot{} equals to {}.'.format(temp, mpmath.cot(angle))
        elif computingAction == "5":
            angle = float(input("Enter the angle in degrees: "))
            temp = angle
            angle = (angle * pi) / 180
            result = '{} degrees equals to {} radians.'.format(temp, angle)
        elif computingAction == "6":
            angle = float(input("Enter the angle in radians: "))
            temp = angle
            angle = (angle * 180) / pi
            result = '{} radians equals to {} degrees.'.format(temp, angle)
        elif computingAction == "7":
            continue
        else:
            result = "Choose from the options."
        print(result)
    #______________________________________________________________
    #End trigonometric ratios

    elif selection == "3" or selection == "Statistics" or selection == "statistics":
        print("***In this section, you enter a list of numbers and get mean, mode, and median.***")
        counter = 1
        numbers_list = []
        while True:
            numberOfNumbers = int(input("Enter the number of numbers: "))
            if numberOfNumbers <= 0:
                print("Invalid input")
            else:
                for i in range(numberOfNumbers):
                    print(f'{counter:<3}', end="")
                    number = float(input("Enter number: "))
                    numbers_list.append(number)
                    counter += 1
                continueOrNot = input("""Do you continue or not?
                1.Yes
                2.No
                >>>>""")
                if continueOrNot == "1" or continueOrNot == "Yes" or continueOrNot == "yes":
                    continue
                elif continueOrNot == "2" or continueOrNot == "No" or continueOrNot == "no":
                    mean = 'The average of the list is equal to {}'.format(statistics.mean(numbers_list))
                    mode = 'The mode of the list is equal to {}'.format(statistics.mode(numbers_list))
                    median = 'The median of the list is equal to {}'.format(statistics.median(numbers_list))
                    print(mean, mode, median, sep="\n")
                    break
                else:
                    counter = 1
                    numbers_list = []
                    print("Choose from the options.")
                    print("***In this section, you enter a list of numbers and get mean, mode, and median.***")


    elif selection =="4" or selection == "Exit" or selection == "exit":
        break










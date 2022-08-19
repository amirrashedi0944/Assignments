while True:
    hoursToSeconds = 0
    secondsToHours = 0
    selection = input('''
1.Hours to seconds
2.Seconds to hours
3.Exit
>>>>''')
    if selection == "1":
        hours = int(input("Enter the hour: "))
        if hours < 0 or hours > 24:
            print("Hours must be between 0 and 24.")
            continue
        else:
            minutes = int(input("Enter the minutes: "))
            if minutes < 0 or minutes >= 60:
                print("Minutes must be between 0 and 59.")
                continue
            else:
                seconds = int(input("Enter the seconds: "))
                if seconds < 0 or seconds >= 60:
                    print("Seconds must be between 0 and 59.")
                    continue
                else:
                    hoursToSeconds = (hours * 3600) + (minutes * 60) + (seconds)
        print(f'{hours}:{minutes}:{seconds}')
        print(f'It is equals to {hoursToSeconds} seconds.')
    elif selection == "2":
        secondsToHours = int(input("Enter the time in seconds: "))
        if secondsToHours < 0 or secondsToHours >= 90000:
            print("The time in seconds must be between 0 and 89999.")
            continue
        else:
            hours = secondsToHours // 3600
            secondsToHours = secondsToHours % 3600
            minutes = secondsToHours // 60
            secondsToHours = secondsToHours % 60
            seconds = secondsToHours
            print(f'{hours}:{minutes}:{seconds}')
    elif selection == "3":
        break
    else:
        print("Choose from the options.")
        continue

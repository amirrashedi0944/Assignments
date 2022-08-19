import random as rnd
import time
numberOfGuess = 1
startOfInterval = 1
endOfInterval = 99

startContext = "Imagine a number between 1 and 99 in your mind."
for character in startContext:
    time.sleep(0.03)
    print(character, flush=False, end="")

result = rnd.randint(1, 99)
userAnswer = "Initial value"
while True:
    continueContext = '''\n\tHmmmmmmmmmm!!!
    Is the number {} ?'''.format(result)
    for character in continueContext:
        time.sleep(0.01)
        print(character, flush=False, end="")

    userAnswer = input("""
    1.Yes, it is.
    2.No, it's bigger.
    3.No, it's smaller
    >>>>>""")

    if userAnswer == "1" or userAnswer == "Yes" or userAnswer == "yes":
        break
    elif userAnswer == "2" or userAnswer == "Bigger" or userAnswer == "bigger":
        startOfInterval = result
        result = rnd.randint(startOfInterval+1, endOfInterval-1)
        numberOfGuess += 1
    elif userAnswer == "3" or userAnswer == "Smaller" or userAnswer == "smaller":
        endOfInterval = result
        result = rnd.randint(startOfInterval+1, endOfInterval-1)
        numberOfGuess += 1
    else:
        print("Invalid input.")

endContext = '''Horaaaaaaaaaaaaaaa!!!
The computer won with {} guesses. '''.format(numberOfGuess)
for character in endContext:
    time.sleep(0.02)
    print(character, flush=False, end="")

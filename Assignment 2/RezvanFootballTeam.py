rezvanWins = 0
rezvanTied = 0
rezvanLosses = 0
rezvanPoints = 0
numberOfGames = 1
while numberOfGames != 5:
    print(f'Game {numberOfGames}')
    game = input("""*****************
    Win     ---> +3 points
    Tied    ---> +1 points
    Lose    ---> +0 points
    Enter the team point in this match: """)
    type(game)
    match game:
        case "3":
            rezvanWins += 1
            rezvanPoints += 3
        case "1":
            rezvanTied += 1
            rezvanPoints += 1
        case "0":
            rezvanLosses += 1
        case _:
            print("Invalid input.")
            numberOfGames -= 1
    numberOfGames += 1
print(f'Number of team wins = {rezvanWins}')
print(f'Number of team losses = {rezvanLosses}')
print(f'Number of team tied games = {rezvanTied}')
print(f'Points of team = {rezvanPoints}')

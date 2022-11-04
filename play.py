import os
from pathlib import Path

while True:
    valid_game = False
    print("\nWhich game do you want to play?")
    print("1 Wordle\n2 Hangman\n3 TicTacToe (2 player)")

    while valid_game == False:
        try:
            game = int(input("\nEnter game number: "))
        except:
            print("Enter a number.")
            continue

        if game in [1,2,3]:
            valid_game = True

        if game == 1:
            path = Path(r"./wordle")
        elif game == 2:
            path = Path(r'./hangman')
        elif game == 3:
            path = Path(r'./NandC')
        else:
            print("Not a valid game number")

    os.chdir(path)
    run = r'run.py'
    print(os.getcwd())
    exec(open(run).read())

    os.chdir('..')
    again = input("Do you want to play something else? [y/n]: ")
    if again == 'n':
        break
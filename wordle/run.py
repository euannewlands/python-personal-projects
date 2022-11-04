from wordle.wordleFiles.wordle import run  
# run game on loop
play = True
while play == True:
    game = run()
    ask = input("Do you want to play again [y/n]? ")
    if ask != 'y':
        print("Thanks for playing!")
        play = False
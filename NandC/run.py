from NaughtsCrosses import NaughtsAndCrosses

play = True
while play == True:
    game = NaughtsAndCrosses() # restarts game with clean board
    game.play()
    ask = input("Do you want to play again [y/n]? ")
    if ask != 'y':
        "Thanks for playing!"
        play = False
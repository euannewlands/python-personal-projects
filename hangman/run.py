from hangman.hangman import Hangman

play = True
print("\nLet's play Hangman!")
while play == True:
    game = Hangman() # restarts game with clean board
    game.main_loop()
    ask = input("Do you want to play again [y/n]? ")
    if ask != 'y':
        "Thanks for playing!"
        play = False
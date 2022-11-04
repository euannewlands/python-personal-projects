import random
import string

class Hangman_Design:
    HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', 
'''
 +---+
 O   |
     |
     |
    ===''',  
 '''
 +---+
 O   |
 |   |
     |
    ===''', 
 '''
 +---+
 O   |
 |\  |
     |
    ===''', 
'''
 +---+
 O   |
/|\  |
     |
    ===''', 
'''
 +---+
 O   |
/|\  |
/ \  |
    ===''',
'''
 +---+
 X   |
/|\  |
/ \  |
    ===''']


class Hangman(Hangman_Design):
    def __init__(self):
        print("Guess the word to save Eric from being hanged!")
        self.word = self.choose_word()

    @staticmethod       # doesn't interact with class or instance variables
    def choose_word():
        f = open("hangman.txt", 'r')
        words = f.readlines()
        word = words[random.randint(0,len(words)-1)]
        return word.replace('\n','')

    def take_guess(self):
        ''' DESCRIPTION: Asks user for a guess, valid guess is a letter.
            PARAMS: self
            RETURNS: guess [str] - valid user guess
        '''
        guess = None
        while guess == None:
            guess = input("\nGuess a letter: ")
            try:
                self.init_user_keyboard().index(guess.upper())  # check guess is a valid letter
            except:
                print("Invalid guess. Input a single letter.")
                guess = None
            # TODO: check against remaining potential letters. Needs updated keyboard function
        
        return guess

    def check_guess(self, guess):
        word_letters = [letter.upper() for letter in self.word]

        if guess.upper() in word_letters:
                return self.find_all_occurences(guess, word_letters), guess.upper()
        return None, None

    def find_all_occurences(self, guess, word_letter_list):
        return [i for i, l in enumerate(word_letter_list) if l == guess.upper()]

    def update_display(self, guess = None, prev_display = None):
        if guess == None:
            return self.empty_word_display()
        else:
            idxs, letter = self.check_guess(guess)
            display = []
            if idxs != None:
                for i, l in enumerate(range(len(prev_display))):
                    if i in idxs:
                        print(letter.upper(), end = ' ')
                        display.append(letter.upper())
                    elif prev_display[i] != '_':
                        print(prev_display[i], end = ' ')
                        display.append(prev_display[i])
                    else:
                        print('_', end = ' ')
                        display.append('_')
                print('\n')
                return display
            else:
                for i in range(len(prev_display)):
                    print(prev_display[i], end = ' ')
                print('\n')
                return prev_display

    def empty_word_display(self):
        display = []
        for l in range(len(self.word)):
            print("_ ", end = '')
            display.append('_')
        print('\n')
        return display

    @staticmethod
    def init_user_keyboard():
        '''DESCRIPTION: Function initialises a keyboard that will be used to help users select letters they have not already used
    
            PARAMS: None
    
            RETURNS: letters [list] - letters of the alphabet
    '''
        letters = []
        for letter in string.ascii_uppercase:
            letters.append(letter)
        return letters

    def update_keyboard(self, guess, keyboard):
        if guess.upper() not in self.word.upper():
            try:
                keyboard.remove(guess.upper())
            except:
                print("Careful.. that letter has already been incorrectly guessed.")
        return keyboard

    def check_win(self, display):
        return [letter.upper() for letter in self.word] == display


    def main_loop(self):
        alive = True
        stages = 0
        guess = None
        display = None
        keyboard = self.init_user_keyboard()

        while alive == True:
            print(Hangman.HANGMAN_PICS[stages])
            display = self.update_display(guess, display)

            if self.check_win(display) == True:
                print("You saved Eric!\n")
                break
            print("Potential letters: ", ' '.join(keyboard))
            print('\n')
            guess = self.take_guess()
            correct_letter = self.check_guess(guess)[0]
            
            if correct_letter == None:
                stages += 1
            if stages == 6:
                alive = False
                print(Hangman.HANGMAN_PICS[stages])
                print(f"Eric is dead... the word was {self.word}.\n")
                break

            keyboard = self.update_keyboard(guess, keyboard)

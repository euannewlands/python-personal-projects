import os
from os import lseek
import random
import string

class bcolors:
    '''NAME: bcolours - basic colours (green yellow red)... google ANSI codes for details...
    
    DESCRIPTION:  Class to turn print(<str>) to some basic colours (green, yellow, red) to give user clues.
                  If colours are difficult to see, try changing terminal colour theme.

    ATTRIBUTES:
    -- including in string will colour subsequent text [colour] --
    CORRECT -- green; letter is in correct position
    HINT -- yellow; letter is in word, but not correct position
    BLANK -- red; letter is NOT in word
    RESET -- default; returns text colour to default

    EXAMPLE:
    x = 'f{bcolors.CORRECT}hi my name is{bcolors.RESET} jeff'
    print(x) >>> [hi my name is: GREEN TEXT] [jeff: DEFAULT TEXT]
    '''

    CORRECT = '\033[1;32;40m' #black background, green text
    HINT = '\033[1;33;40m' #black background, yellow text
    BLANK = '\033[1;37;40m' #black backgroun, white text
    RESET = '\033[0m' #RESET COLOR

    '''
    If you want to test this out yourself, create a code cell and type `print("\033[92m hello")`
    What happens? now type `print("hello")` Is that what you expect?
    Reset with print("\033[0m")
    '''

def select_word_of_the_day():
    '''DESCRIPTION: Function selects a random word from a text file with 2315 possibilities

    PARAMS: None

    RETURNS: wotd [str] - word of the day, a randomly selected 5 letter word from text file
    '''
    # open file, convert line entries to lists, close file
    word_bank = open(os.getcwd() + '/wordleFiles/wordle_solutions.txt', 'r')
    word_bank_words = word_bank.readlines()
    word_bank.close()
    
    # select a random word from the list, edit string to match user guess format (removes '\n')
    wotd_idx = random.randint(0,len(word_bank_words)-1)
    wotd = word_bank_words[wotd_idx].replace("\n","")

    return wotd

def check_real_word(guess):
    '''DESCRIPTION: Function to check the user's guess exists in the dictionary of all 5 letter words.
    
    PARAMS: guess [str] - user's 5 letter word guess

    RETURNS: [bool] - returns True if word is a valid guess, else return False
    '''
    wordle_dictionary = open(os.getcwd() + '/wordleFiles/wordle_complete_dictionary.txt', 'r')
    for word in wordle_dictionary:      # loop compares user guess to valid words
        if guess.lower() == word.lower().replace('\n',''):  # removes the extra line in text to ensure words are same format / comparable
            return True
    return False

def initialise_keyboard():
    '''DESCRIPTION: Function initialises a keyboard that will be used to help users select letters they have not already used
    
    PARAMS: None
    
    RETURNS: letters [list] - letters of the alphabet
    '''
    letters = []
    for letter in string.ascii_uppercase:
        letters.append(letter)
    return letters

def update_keyboard(guess_letter, latest_keyboard):
    '''DESCRIPTION: Function to remove letters from the keyboard hint. 
    Only used when guess_letter is identified as INCORRECT in check_guess().
    
    PARAMS: guess_letter [str] - the letter to remove from the keyboard hint
            latest_keyboard [list] - latest keyboard hint to remove from
        
    RETURNS: latest_keyboard [list] - keyboard with the removed letter'''
    # bypass error when trying to remove letter that has already been removed (when user guesses incorrect letter twice)
    try:
        latest_keyboard.remove(guess_letter.upper())
    except:
        pass
    
    return latest_keyboard

def wotd_letter_count(wotd):
    ''' DESCRIPTION: Function counts the  occurences of the letter in the WotD. Used to select letter hints in colour_hints()

    PARAMS: wotd [str] - word of the day
    
    RETURNS: letter_count [dict] - keys; letter | values; count in wotd'''
    letter_count = {}
    for letter in wotd:
        letter_count[letter] = wotd.count(letter)
    return letter_count

def colour_hints(wotd, guess):
    '''DESCRIPTION: Function reviews a single guess from the user and returns guess with coloured hints, to inform next guess.
    Function will not give in-word hint for double letter if double letter not in Word of the Day. Returns list of hint colours.
    
    PARAMS: wotd [str] - word of the day
            guess [str] - user's guess
    RETURNS: final_colours [list] - list of hint colours for each letter in guess word
    '''
    
    wotd_letters = wotd_letter_count(wotd)  # [dict] occurrences of letters in wotd, used to reference how many in_word hints to allow per letter
    final_colours = [bcolors.BLANK]*5     # all blank until identified as otherwise
    guess_letters = ['']*5  # empty list of length 5, used to prevent in_word hints if letter already been hinted (correct or in_word)

    # check through all of guess: prioritise green
    for i, letter in enumerate(guess):      # checks letter position against WotD. Enumerate gives count of iteration. Try print(enumerate(guess))
                                            # See url{https://www.programiz.com/python-programming/methods/built-in/enumerate} for enumerate documentation
        if letter.lower() == wotd[i]:
            final_colours[i] = bcolors.CORRECT              # inform colour of letter
            guess_letters[i] = letter.lower()   # to count occurences to determine yellows

    # check through all of guess: turn letter yellow if letter count so far < total letter count in WotD
    for i, letter in enumerate(guess):
        try:
            if (final_colours[i] != bcolors.CORRECT) and (guess_letters.count(letter.lower()) < wotd_letters[letter.lower()]):
                guess_letters[i] = letter.lower()
                final_colours[i] = bcolors.HINT
        except:
            pass    # error will occur if (guess) letter not in wotd_letters.keys()

    return final_colours


def ask_for_guess(wotd):
    '''DESCRIPTION: Function asks user for their input, allowing them 6 guesses to guess the word. 
    Calls other functions to check word validity.

    PARAMS: wotd [str] - randomly selected word of the day

    RETURNS: answer [bool] - Returns False if after 6 guesses, user has not guessed word
    '''
    user_keyboard = initialise_keyboard()   # initialise keyboard hint with complete alphabet
    print("\n")  # format output with some white space

    all_guess = []
    for attempts in range(1,7):
        guess = None
        print("Potential letters:", ' '.join(user_keyboard))
        
        while guess == None:           # while loop to make sure guess is valid word
            guess = input(f"Attempt {attempts}: ")
            try:
                if check_real_word(guess) == False:     # ensure guess is a real word (and 5 letters)
                    raise Exception()
            except:
                print(f"{guess} is not a valid word.\n")
                guess = None                            # none to ensure loop runs until valid word entered

        answer, user_keyboard, guess_output = check_guess(guess, wotd, user_keyboard)   # compare answer to WotD and print HINTS
        all_guess.append(guess_output)
        display_guess(all_guess, attempts)

        if answer == True:
            print(f"\nYou guessed the word in {attempts} attempts!\n")
            break                                                               # break ends game
        print('\n')     # print new line after each guess
        
    return answer


def display_guess(all_guess, attempt):
    '''Function to mimic the output of the wordle game'''
    for word_i in range(attempt):
        for letter_i in all_guess[word_i]:
            print(letter_i, end='')
        print('\n')

    for rows in range(1, 7 - attempt):
        print('- - - - -')


def check_guess(guess, wotd, user_keyboard):
    '''DESCRIPTION: Function reviews a single guess from the user and returns guess with coloured hints, to inform next guess.
                    Function removes incorrect letters from user's keyboard hint visual.

    PARAMS: guess [str] - user's 5-letter word guess
            wotd [str] - the randomly selected word
            user_keyboard [list] - keyboard hint; alphabet minus letters incorrectly guessed by the user

    RETURNS: answer[bool] - True if guess == Word of the Day
             user_keyboard [list] - Updated keyboard hint for if guess included incorrect letters
    '''
    guess_output = []                           # dictionary to store formatted guess
    
    hint_colours = colour_hints(wotd,guess)  # returns coloured hints to inform next guess

    for i in range(len(guess)):
        guess_output.append(hint_colours[i] + guess[i].upper() + bcolors.RESET + ' ')
        if guess[i].lower() not in wotd:
            user_keyboard = update_keyboard(guess[i].upper(), user_keyboard)

    return guess.lower() == wotd.lower(), user_keyboard, guess_output 


def run():
    wotd = select_word_of_the_day()
    success = ask_for_guess(wotd)
    if success == False:
        print(f"The word was {wotd.upper()}. Better luck next time!\n")
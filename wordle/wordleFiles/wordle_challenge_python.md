# Create your own Wordle clone in Python

Instructions:

1) You can download the dictionary (wordle_complete_dictionary.txt) and the word bank (wordle_solutions.txt) from here: <https://github.com/AllValley/WordleDictionary>
2) Read from the files and load the data into Python
3) Choose a random word from the word bank as the chosen word for the day.
4) Write the logic for the Wordle game
   - Write a loop to go through the guesses from the user.
   - For each guess, you may have to write an inner loop that runs until the user enters a valid guess. Once a valid guess is entered, compare the guess against the chosen word and provide clues to the user.
   - Be creative while providing the clues (you can use coloured letters to encode the clue or perhaps you may want to use some symbols for clues (e.g. ~C~ R A ~N~ -E-)). You can write this comparison logic as a function so that it can be reused for each guess.
   - If the user guesses correctly, you break out of the loop and provide the result to the user.

import wordle

def test_wordle():
    for i in range(5000):
        wotd = wordle.select_word_of_the_day()
        assert len(wotd) == 5    # word is 5 characters
        assert wordle.check_real_word(wotd) == True
        assert len(wordle.initialise_keyboard()) == 26
        assert len(wordle.update_keyboard('a', wordle.initialise_keyboard())) == 25
        assert wordle.wotd_letter_count('booze') == {'b': 1, 'o': 2, 'z': 1, 'e':1}
        assert wordle.colour_hints(wotd, wotd) == [wordle.bcolors.CORRECT]*5

        assert wordle.check_guess(wotd, wotd, wordle.initialise_keyboard())[0] == True
        assert len(wordle.check_guess(wotd, wotd, wordle.initialise_keyboard())[1]) == 26
        assert len(wordle.check_guess(wotd, wotd, wordle.initialise_keyboard())[2]) == 5 




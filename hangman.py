# import statements
from lib import dictionary_organised
from lib.dictionary_organised import *
from random import choice
from utils.strings import find_chars_in_str, replace_index_str

# Settings

# General
symbol = '*'
termination_code = '%'

# for 1-player mode
overall_difficulty = 20         # [lowest (most difficult)] 14 ===========> 29 [highest (easiest)]
minimum_num_of_letters = 3
maximum_num_of_letters = 8
wordsList = [three_letter_words, four_letter_words, five_letter_words, six_letter_words, seven_letter_words, eight_letter_words]

# for 2-player game mode
words = ["second", "words"]
clues = [None, None]
customAttempts = [6, 5]

# /Settings

# Game
terminate = False
while not terminate:
    # Operation
    terminate = False
    proceedGame = True

    # Introduction
    print('\nWelcome to the Hangman Game!')
    prior_xp = input('Have you played Hangman before?\n> ').strip().lower()

    # Overview of Hangman
    if prior_xp == 'no':
        print('\nOverview:')
        print('Hangman is a game where a player tries to figure out a word by guessing certain letters in the word.')
        print('If the letter is present(either once or multiple times), the positions of all of that letter in the word will be revealed.')
        print('Otherwise, one attempt for guessing will be deducted from the player\'s total remaining guesses.')

    # Rules of this version
    print('\nThese are the rules for this Hangman Game:')
    print('> you may only type one letter per guess')
    print(f'> each "{symbol}" represents a letter')
    print('> you lose an attempt if you guess wrongly or if you do not comply with the rules')
    print('> the revealed letters and your attempts remaining will be displayed below your guess')
    print('Good luck! :)')

    # Number of players
    while not terminate:
        players = (input('\nPlease input the number of players(1 or >1) in the space below.\nPlayers: ').strip())
        # forced termination
        if players == termination_code:
            terminate = True
            break
        # 1-player mode
        elif players == '1':
            print('\nPlease enter your desired word length:')
            print('\r > enter "any" to accept any word /')
            print('\r > enter an integer from 3 to 7 to indicate the length of the word')
            while True:
                try:
                    word_length_str = input('\r Word length: ').strip().lower()
                    if word_length_str == termination_code:
                        terminate = True
                        break
                    elif word_length_str == 'any':
                        word = choice(choice(wordsList))
                        word.strip().lower()
                        break
                    elif len(word_length_str) > 1:
                        print('Invalid input!')
                    else:
                        word_length_int = int(word_length_str)
                        if (word_length_int >= minimum_num_of_letters) and (word_length_int <= maximum_num_of_letters):
                            word = choice(wordsList[word_length_int - 3])
                            wordsList[word_length_int - 3].remove(word)
                            break
                        else:
                            print(f'Please enter an integer between {minimum_num_of_letters} and {maximum_num_of_letters} (inclusive)')
                except ValueError:
                    print('Please only enter either a number or "any"!')
                except NameError:
                    print('Please only enter either a number or "any"!')
            print('\nPlease choose a difficulty level from 1 to 5 (with 1 being the easiest)')
            while True:
                try:
                    level = int(input('\nLevel: '))
                    if (level >= 1) and (level <= 5):
                        break
                    elif level < 0:
                        print('Level cannot be less than 1!')
                    elif level > 5:
                        print('Level cannot be more than 5!')
                except ValueError:
                    print('Please only enter an integer from 1 to 5!')
                except NameError:
                    print('Please only enter an integer from 1 to 5!')
            attempts = overall_difficulty - word_length_int - level
            proceedGame = True
            break
        # multi-player mode
        elif players == '>1':
            # word is extracted from back of words array
            word = words[-1]
            words.pop()
            word_length_int = len(word)
            # number of attempts is extracted from back of customAttempts array
            attempts = customAttempts[-1]
            customAttempts.pop()
            print(f'Clues: {clues[-1]}')
            clues.pop()
            proceedGame = True
            break
        # error checking
        else:
            print('Please do not type anything other than "1" or ">1"!')
            proceedGame = False

    # Hangman Program
    if proceedGame:
        # making a copy of the word to check repeated guesses
        lettersLeftToGuess = word
        # encoding the word
        revealed_letters = symbol * word_length_int
        attemptNum = 0
        print('----------------------')
        print(f'Word: {revealed_letters}')
        print(f'Number of letters: {word_length_int}')
        print(f'Attempts: {attempts - attemptNum}\n')
        while attemptNum < attempts:
            guess = input('Guess: ').strip().lower()
            # forced termination
            if guess == termination_code:
                break
            # checking size of input
            elif len(guess) > 1:
                attemptNum += 1
                print(f'Guess must be one letter only!')
                print(f'Attempts left: {attempts - attemptNum}\n')
            # checking if guess is correct
            else:
                if guess in word:
                    # checking if the guess has already been made
                    if guess in lettersLeftToGuess:
                        for charIndex in find_chars_in_str(word, guess):
                            revealed_letters = replace_index_str(revealed_letters, guess, charIndex)
                            lettersLeftToGuess = replace_index_str(lettersLeftToGuess, symbol, charIndex)
                        print(f'Word: {revealed_letters}')
                        print(f'Attempts left: {attempts - attemptNum}\n')
                        # success
                        if revealed_letters == word:
                            print(f'Congratulations, you have found the word \"{word}\" successfully!')
                            break
                    else:
                        print(f'You have already guessed "{guess}".\n')
                else:
                    attemptNum += 1
                    print(f'Sorry; the word does not include "{guess}".')
                    if attemptNum < attempts:
                        print(f'Attempts left: {attempts - attemptNum}\n')
                    # failure
                    else:
                        print('\nYou have exhausted all your attempts. Try again next time!')
                        print(f'The answer was "{word}". :)')
    # Another game
    print('\nDo you wish to continue?')
    terminate = ((input('> ').strip().lower()) == 'no')
# /Game

# Goodbye message
print("\nThank you for playing Hangman!\n\t\xa9 python \xa9")

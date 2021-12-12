# Project available at https://hyperskill.org/projects/69

import random

print('H A N G M A N')

def game_menu():
    menu = input('Type "play" to play the game, "exit" to quit: ')
    try:
        if menu == 'play':
            play_game()
        elif menu == 'exit':
            None
        else:
            raise ValueError
    except ValueError:
        game_menu()

def play_game():
    words = ['python', 'java', 'kotlin', 'javascript']
    winning_word = random.choice(words)
    letters = (len(winning_word)) * '-'

    letters_list = list(letters)
    winning_word_set = set(winning_word)
    not_in_winning_word = []

    tries = 8
    while tries > 0:
        joined_letters = ''.join(letters_list)
        print()
        print(joined_letters)
        guess = input(f'Input a letter: ')
        winning_word_set = set(winning_word)
        if len(guess) > 1:
            print('You should input a single letter')
        elif len(guess) <= 1 and not guess.islower():
            print('Please enter a lowercase English letter')
        elif guess in joined_letters:
            print("You've already guessed this letter")
        elif guess in not_in_winning_word:
            print("You've already guessed this letter")
        elif guess in winning_word_set:
            for index, letter in enumerate(winning_word):
                if guess == letter:
                    letters_list[index] = guess
                    if ''.join(letters_list) == winning_word:
                        joined_letters = ''.join(letters_list)
                        tries = 0
                        break
        else:
            not_in_winning_word.append(guess)  # add incorrect letter to a list to be checked
            print("That letter doesn't appear in the word")
            tries -= 1

    if joined_letters == winning_word and tries == 0:
        print()
        print(joined_letters)
        print('You guessed the word!')
        print('You survived!')
    else:
        print('You lost!')
        
        
# Game execution
if __name__ == "__main__":
    game_menu()
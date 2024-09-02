import random
import os

from animals import animal_words
from plants import plant_words
from planets import planet_words


def ascii_wordhunt():
    print(r"""
     _        __              ____  __            __
    | |     / /___  _________/ / / / /_  ______  / /_
    | | /| / / __ \/ ___/ __  / /_/ / / / / __ \/ __/
    | |/ |/ / /_/ / /  / /_/ / __  / /_/ / / / / /_
    |__/|__/\____/_/   \__,_/_/ /_/\__,_/_/ /_/\__/

    """)


def ascii_goodbye():
    print(r"""

       ______                ____               __
      / ____/___  ____  ____/ / /_  __  _____  / /
     / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ /
    / /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/
    \____/\____/\____/\__,_/_.___/\__, /\___(_)
                                 /____/

    """)


def ascii_instructions():
    print(r"""

        __  __                 __             ____  __           ___
       / / / /___ _      __   / /_____       / __ \/ /___ ___  _/__ \
      / /_/ / __ \ | /| / /  / __/ __ \     / /_/ / / __ `/ / / // _/
     / __  / /_/ / |/ |/ /  / /_/ /_/ /    / ____/ / /_/ / /_/ //_/
    /_/ /_/\____/|__/|__/   \__/\____/    /_/   /_/\__,_/\__, /(_)
                                                        /____/
    """)


def instructions():
    ascii_instructions()
    print("- You will have a choice of THREE categories.\n")
    print("- The categories include: plants, animals and planets.\n")
    print("- Once you have chosen, you will be presented"
          "with a word to guess.\n")
    print("- Please ensure your guesses are single letters only.\n")
    print("- The number of guesses is the number of letters"
          "in the word plus two extra chances.\n")
    print("Press 'r' key to return")
    get_instructions_input()


def get_instructions_input():
    user_input = input()

    if user_input == "r":
        clear_terminal()
        return welcome()
    else:
        print("Press 'r' key to return")
        return get_instructions_input()


def instructions_or_start():
    user_input = input()
    if user_input == "i":
        instructions()
    elif user_input == "s":
        play_wordhunt()
    else:
        print("Please choose 's' or 'i' only")
        return instructions_or_start()


def welcome():
    ascii_wordhunt()
    print("Welcome to WordHunt!\n")
    print("Press 'i' for instructions or press 's' to start")

    instructions_or_start()


def enter_wordhunt():
    welcome()


def get_username():
    username = input()
    if len(username) > 1 and username.isalpha():
        return username
    else:
        print("Please enter at least two letters")
        return get_username()


def play_wordhunt():
    clear_terminal()
    print("Happy hunting!\n")
    print("Please type your name...")
    name = get_username()
    clear_terminal()

    print("Good Luck, lets get started", name)
    words = get_category_words()
    active_word = random.choice(words)

    guesses = []
    number_guesses = number_letters(active_word) + 2
    number_attempts = 0
    active_word_length = len(active_word)

    print(f"Let's hunt - you have {number_guesses} "
          "attempts to guess the word:")
    print(f"Your word has {active_word_length} letters:")

    current_status = ''
    for x in range(active_word_length):
        current_status += ' _'

    print(current_status.strip())

    while number_attempts < number_guesses:
        current_status = get_current_status(active_word, guesses)

        if number_attempts > 0:
            clear_terminal()
            print("So far you have found:")
            print(current_status)
            if (number_attempts is number_guesses - 1):
                print(f"You have 1 guess left")
            else:
                print(f"You have {number_guesses - number_attempts} "
                      "guesses left")

            print("Choose your next letter")
        else:
            print("Choose your first letter")

        number_attempts += 1

        guess = get_user_guess(guesses)
        guesses.append(guess)
        current_status = get_current_status(active_word, guesses)

        if current_status == active_word:
            clear_terminal()
            print("Well done - you found the word!")
            print(current_status)
            restart_or_exit(name)

    clear_terminal()
    print("Hard luck, you are out of guesses")
    print(current_status)
    print("The word was", active_word)
    restart_or_exit(name)


def get_current_status(active_word, guesses):
    current_status = ''

    for letter in active_word:
        if letter.lower() in guesses:
            current_status += letter
        else:
            current_status += ' _'
    return current_status.strip()


def number_letters(word):
    return len(set(word.lower()))


def get_user_guess(existing_guesses):
    guess = input()
    if guess in existing_guesses:
        print(f"You have already picked {guess}")
        print("Try a new letter")
        return get_user_guess(existing_guesses)
    elif not guess.isalpha():
        print("Please choose a letter")
        return get_user_guess(existing_guesses)
    elif len(guess) > 1:
        print("Please choose one letter only")
        return get_user_guess(existing_guesses)
    else:
        return guess


def get_category_words():
    print("\nPlease choose a category:\n")

    print("type a for PLANTS\n")
    print("type b for ANIMALS\n")
    print("type c for PLANETS\n")
    category_choice = input()

    if category_choice == "a":
        clear_terminal()
        print("\nYou chose PLANTS\n")
        return plant_words
    elif category_choice == "b":
        clear_terminal()
        print("\nYou chose ANIMALS\n")
        return animal_words
    elif category_choice == "c":
        clear_terminal()
        print("\nYou chose PLANETS\n")
        return planet_words
    else:
        print("Please choose a valid category")
        return get_category_words()


def restart_or_exit(name):
    print(f"Would you like to play again, {name}?")
    print("Press y for yes, n for no")
    answer = input()
    if (answer == 'y'):
        clear_terminal()
        play_wordhunt(name)
    else:
        clear_terminal()
        ascii_goodbye()
        exit(1)


def clear_terminal():
    os.system('cls || clear')


if __name__ == '__main__':
    enter_wordhunt()

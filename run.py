import random
import os

from animals import animal_words
from plants import plant_words
from planets import planet_words
from ascii import ascii_wordhunt, ascii_instructions, ascii_goodbye


def instructions():
    clear_terminal()
    ascii_instructions()
    print("- You will have a choice of THREE categories.\n")
    print("- The categories include: plants, animals and planets.\n")
    print("- Once you have chosen, you will be presented"
          " with a word to guess.\n")
    print("- Please ensure your guesses are single letters only.\n")
    print("- The number of guesses is the number of letters"
          " in the word plus TWO more chances.\n")
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
          "attempts to guess the word:\n")
    print(f"Your word has {active_word_length} letters:\n")

    current_status = ''
    for x in range(active_word_length):
        current_status += ' _'

    print(f"{current_status.strip()}\n")

    while number_attempts < number_guesses:
        current_status = get_current_status(active_word, guesses)

        if number_attempts > 0:
            clear_terminal()
            print("So far you have found:\n")
            print(f"{current_status}\n")
            if (number_attempts is number_guesses - 1):
                print(f"You have 1 guess left\n")
            else:
                print(f"You have {number_guesses - number_attempts} "
                      "guesses left\n")

            print("Choose your next letter\n")
        else:
            print("Choose your first letter\n")

        number_attempts += 1

        guess = get_user_guess(guesses)
        guesses.append(guess)
        current_status = get_current_status(active_word, guesses)

        if current_status == active_word:
            clear_terminal()
            print("Well done - you found the word!\n")
            print(current_status)
            restart_or_exit(name)

    clear_terminal()
    print("Hard luck, you are out of guesses\n")
    print(current_status)
    print(f"The word was {active_word}\n")
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
        print(f"You have already picked {guess}\n")
        print("Try a new letter\n")
        return get_user_guess(existing_guesses)
    elif not guess.isalpha():
        print("Please choose a letter\n")
        return get_user_guess(existing_guesses)
    elif len(guess) > 1:
        print("Please choose one letter only\n")
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
        print("Please choose a valid category\n")
        return get_category_words()


def restart_or_exit(name):
    print(f"Would you like to play again, {name}?\n")
    print("Press y for yes, n for no\n")
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

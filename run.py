import random
import os

from animals import animal_words
from plants import plant_words
from planets import planet_words


def welcome():
    print("Welcome to WordHunt!\n")
    print("How to play?")
    print("You will have a choice of THREE categories.")
    print("Once you have chosen, you will be presented with a word to guess.")
    print("Please ensure your guesses are single letters only.\n")
    print("Happy hunting!\n")


def enter_wordhunt():
    welcome()
    print("Please type your name...")
    name = get_username()
    clear_terminal()

    print("Good Luck, lets get started", name)
    play_wordhunt(name)


def get_username():
    username = input()
    if len(username) > 1 and username.isalpha():
        return username
    else:
        print("Please enter at least two letters")
        return get_username()


def play_wordhunt(name):
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
        exit(1)


def clear_terminal():
    os.system('cls || clear')


if __name__ == '__main__':
    enter_wordhunt()

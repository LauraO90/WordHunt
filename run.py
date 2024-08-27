import random

from animals import animal_words
from plants import plant_words
from planets import planet_words


def enter_wordhunt():
    print("Please type your name")
    name = input()

    print("Good Luck, lets get started", name)
    play_wordhunt()


def play_wordhunt():
    words = get_category_words()
    active_word = random.choice(words)

    guesses = []
    number_guesses = number_letters(active_word) + 1
    number_attempts = 0

    print(f"Let's hunt - you have {number_guesses} attempts to guess!")
    current_status = ''
    for x in range(len(active_word)):
        current_status += ' _'

    print(current_status.strip())

    while number_attempts < number_guesses:
        number_attempts += 1

        guess = get_user_guess(guesses)
        guesses.append(guess)

        current_status = ''

        for letter in active_word:
            if letter.lower() in guesses:
                current_status += letter
            else:
                current_status += ' _'
    print(current_status.strip())

    if current_status == active_word:
        print("Well done - you found the word!")
        restart_or_exit()

    print("Hard luck, you are out of guesses")
    print("The word was", active_word)
    restart_or_exit()


def number_letters(word):
    return len(set(word.lower()))


def get_user_guess(existing_guesses):
    guess = input()
    if guess in existing_guesses:
        print(f"You have already picked {guess}")
        print("Try a new letter")
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
        print("\nYou chose PLANTS\n")
        return plant_words
    elif category_choice == "b":
        print("\nYou chose ANIMALS\n")
        return animal_words
    elif category_choice == "c":
        print("\nYou chose PLANETS\n")
        return planet_words
    else:
        print("Please choose a valid category")
        return get_category_words()


def restart_or_exit():
    print("Would you like to play again?")
    print("Press y for yes, n for no")
    answer = input()
    if (answer == 'y'):
        play_wordhunt()
    else:
        exit(1)


if __name__ == '__main__':
    enter_wordhunt()

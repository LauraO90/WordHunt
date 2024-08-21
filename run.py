import random

from animals import animal_words

def start_wordhunt():
    print("Please type your name")
    name = input()

    print("Good Luck, lets get started", name)
    words = get_category_words()
    active_word = random.choice(words)

    print(active_word)
    current_status = ''
    guesses = []

    for x in range(len(active_word)):
        current_status += ' _'
    
    print(current_status.strip())

    guess = input()

    guesses.append(guess)

    current_status = ''

    for letter in active_word:
        if letter.lower() in guesses:
            current_status += letter
        else: 
            current_status += ' _'
    
    print(active_word)
    print(current_status.strip())


def get_category_words():
    print("\nPlease choose a category:\n")

    print("type a for ANIMALS\n")
    category_choice = input()

    if category_choice == "a":
        print("\nYou chose ANIMALS\n")
        return animal_words
    else: 
        print("Please choose a valid category")
        print("type a for ANIMALS\n")
        return get_category_words()

if __name__ == '__main__':
    start_wordhunt()
# Hangman game

import random

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog ' \
        'donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose ' \
        'mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon ' \
        'seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle ' \
        'weasel whale wolf wombat zebra'.split()


def check_win():
    if current_state == objective:
        print("Congratulations! You got it with {} guesses to spare".format(guesses))
        print("The word was: {}".format("".join(current_state)))
        quit()
    else:
        print("Here's how the word looks now: {}".format("".join(current_state)))


def check_letter(letter):
    if letter in objective:
        for letter_index, objective_letter in enumerate(objective):
            if objective_letter == letter:
                current_state[letter_index] = letter
        print("Correct!")
    else:
        print("Incorrect!")

objective = list(words[random.randint(0, len(words) - 1)])
guesses = 10
current_state = list('_')
while len(current_state) < len(objective):
    current_state.append('_')
guessed_letters = []
playing = True
print("Hint: It's an animal")
while playing:
    user_input = input("Guess a letter!\n").lower()
    if user_input not in guessed_letters:
        guessed_letters.append(user_input)
        guessed_letters = sorted(guessed_letters)
        check_letter(user_input)
        check_win()
    else:
        print("You already guessed that letter!")
    guesses -= 1
    print("You have {} guesses left".format(guesses))
    if not guesses:
        print("Try again next time!")
        playing = False

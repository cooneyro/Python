# Guessing game w/ numbers
import random

smallest = 0
largest = 100


def p_exit():
    print("Thanks for playing!")

playing = True
while playing:
    x = random.randint(smallest, largest)
    guessing = True
    print("Hint: It's between {i:0} and {j:0}".format(i=smallest, j=largest))
    while guessing:
        try:
            guess = int(input("Guess the integer! Q to quit.\n"))
            if guess != x:
                print("Too high!") if guess > x else print("Too low!")
            else:
                print("Correct!\n")
                if input("Q to exit or Enter to play again\n").lower() != 'q':
                    guessing = False
                else:
                    p_exit()
                    quit()
        except ValueError:
            if guess.lower() == 'q':
                p_exit()
                quit()
            else:
                print("Error! Please enter an integer value\n")

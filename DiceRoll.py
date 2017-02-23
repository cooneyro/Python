# Simulating a dice roll
import random

playing = True
while playing:
    print("You rolled a {i:0}".format(i=random.randrange(1, 7)))
    if input("Type Y to play again\n") != 'Y':
        playing = False

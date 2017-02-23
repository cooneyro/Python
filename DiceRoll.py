# Simulating a dice roll
import random

playing = True
while playing:
    print("You rolled a {i:0}".format(i=random.randrange(1, 7)))
    playing = input("Type Y to play again\n") == 'Y'

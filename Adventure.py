# Adventure game
# User moves through rooms by inputting text to indicate
# direction they wish to move
# Each room has a description and is connected to 1+ other rooms
# Game tracks direction user is facing and adjusts information
# printed accordingly

# Describing room connections in format
# [ (Name), North, East, South, West ]
# Where North/East etc. denote connected room's position
# based on current room
# Implementation probably could be cleaner
red = ["red", "orange", None, None, None]
green = ["green", None, "orange", None, None]
blue = ["blue", None, "purple", "orange", None]
yellow = ["yellow", "purple", None, None, "orange"]
orange = ["orange", "blue", "yellow", "red", "green"]
purple = ["purple", "black", None, "yellow", "blue"]
end = []

# For string formatting and keeping track of direction user is facing
vowels = ['a', 'e', 'i', 'o', 'u']
go = ['a', 'r', 'b', 'l']
directions = ['in front of you', 'to your right', 'behind you', 'to your left']
facing = ['n', 'e', 's', 'w']
default = 0
first_word = 0
first_letter = 0

# Dict of rooms
rooms = {'red': red,
         'green': green,
         'blue': blue,
         'yellow': yellow,
         'orange': orange,
         'purple': purple,
         'black': end
         }


play = input("Press Enter to play or type Q to quit")
if play.lower() == 'q':
    quit()

print("Type l to go left, r to go right, a to go straight ahead or b to go back")

turns = 1
current_direction = facing[default]
playing = True
current_room = red
while playing:
    if current_room[first_word][first_letter] in vowels:
        begin_vowel = 'n'
    else:
        begin_vowel = ' '
    print("You enter a{} {} room".format(begin_vowel, current_room[default]))
    for w in current_room[1:]:
        if w is not None:
            door_index = ((current_room.index(w)-1) - facing.index(current_direction)) % 4
            door_direction = directions[door_index]
            door_color = current_room[current_room.index(w)]
            if door_color[first_letter] in vowels:
                begin_vowel = 'n'
            else:
                begin_vowel = ' '
            print("There is a{} {} door {}".format(begin_vowel, door_color, door_direction))
    user_go = input("Which direction will you go? \n")
    room_index = facing.index(current_direction) + go.index(user_go) + 1
    if room_index % 4 == 0:
        room_index = 4
    else:
        room_index %= 4
    current_room = rooms[current_room[room_index]]
    current_direction = facing[(facing.index(current_direction) + (go.index(user_go))) % 4]
    if current_room == end:
        print("Congratulations! You reached the end in only {} turns!".format(turns))
        quit()
    else:
        turns += 1

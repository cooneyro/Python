# Adventure game
# User moves through rooms by inputting text to indicate
# direction they wish to move
# Each room has a description and is connected to 1+ other rooms

red = ["red", "orange", None, None, None]
green = ["green", None, "orange", None, None]
blue = ["blue", None, "purple", "orange", None]
yellow = ["yellow", "purple", "orange", None, None]
orange = ["orange", "blue", "yellow", "red", "green"]
purple = ["purple", "end", None, "yellow", "blue"]
end = []

vowels = ['a', 'e', 'i', 'o', 'u']

go = ['a', 'r', 'b', 'l']

directions = ['in front of you', 'to your right', 'behind you', 'to your left']
facing = ['n', 'e', 's', 'w']
rooms = {'red': red,
         'green': green,
         'blue': blue,
         'yellow': yellow,
         'orange': orange,
         'purple': purple,
         'end': end
         }

play = input("Press Enter to play or type Q to quit")
if play.lower() == 'q':
    quit()

print("Type l to go left, r to go right, a to go straight ahead or b to go back")

turns = 1
current_direction = facing[0]
playing = True
current_room = red
while playing:
    if current_room[0][0] in vowels:
        begin_vowel = 'n'
    else:
        begin_vowel = ' '
    print("You enter a{} {} room".format(begin_vowel, current_room[0]))
    for w in current_room[1:]:
        if w is not None:
            door_direction = directions[abs(facing.index(current_direction) - (current_room.index(w)-1)) % 4]
            door_color = current_room[current_room.index(w)]
            if door_color[0] in vowels:
                begin_vowel = 'n'
            else:
                begin_vowel = ' '
            print("There is a{} {} door {}".format(begin_vowel, door_color, door_direction))
    user_go = input("Which direction will you go? \n")
    # current_room = rooms[current_room[((facing.index(current_direction) + go.index(user_go))+1) % 4]]
    # current_room = rooms[current_room[current_direction + current_room[go.index(user_go) % 4]]]
    current_direction = facing[(facing.index(current_direction) + (go.index(user_go))) % 4]
    print(current_direction)
    print(current_room)
    if current_room == end:
        print("Congratulations! You reached the end in only {} turns".format(turns))
        quit()
    else:
        turns += 1

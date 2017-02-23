# Manipulating String

userin = input("Enter a noun, a verb and an adjective separated by spaces\n")

mylist = userin.split()
print("The {} {}ed over the {} person".format(*mylist))

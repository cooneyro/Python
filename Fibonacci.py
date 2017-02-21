# Prints fibonacci numbers 1-10
a, b, c, n = 0, 1, 0, 10
while c < n:
    print("{i:3} : {n:3}".format(i=c+1, n=a))
    a, b = b, a+b
    c += 1


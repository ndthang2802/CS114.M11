import sys


state = -1 

gamers = {}

while state != 0 :

    a = list(map(int,sys.stdin.readline().split()))

    if a[0] == 1:
        gamers[a[1]] = 1
    elif a[0] == 2:
        x = gamers.get(a[1])
        if x :
            print(1)
        else:
            print(0)
    else:
        state = 0

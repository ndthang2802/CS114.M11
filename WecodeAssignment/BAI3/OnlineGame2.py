import sys
 

gamers = {}

try :

    while True:

        a = list(map(int,sys.stdin.readline().split()))

        if a[0] == 1:
            gamers[a[1]] = 1
        elif a[0] == 2:
            x = gamers.get(a[1])
            if x :
                sys.stdout.write('1\n')
            else:
                sys.stdout.write('0\n')    
        elif a[0] == 3:
            x = gamers.get(a[1])
            if x:
                gamers.pop(a[1])
        else:
            break

except :
    pass
        

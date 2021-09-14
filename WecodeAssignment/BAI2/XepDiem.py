test  = int(input())


def soDiemCanMua(n):
    a = 0
    b = 0
    c = 0
    t = 0
    r = 0
    if n >= 4:
        x = n//4
        a = x
        b = x
        c = 2*x
        t = x * 4
        r = n - t
    else:
        a = 1
        b = 1
        c = 0

        t = 2

        r = n-2

    while a + b != c or r > 0 :
        if c < a+b:
            c+=1
            r-=1
            t+=1
        else:
            if a <= b:
                a+=1
                r-=1
                t+=1
            else:
                b+=1
                r-=1
                t+=1
    return t-n

for i in range(test):
    n = int(input())
    print(soDiemCanMua(n))


    

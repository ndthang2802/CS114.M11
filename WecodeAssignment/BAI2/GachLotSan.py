n,m,a = list(map(int,input().split()))

def SoGach(n,m,a):
    
    if n*m <= a*a :
        return 1

    else:
        if n % a != 0:
            n += a - n % a
        if m % a != 0:
            m += a - m % a

        return (n*m) // (a*a)

print(SoGach(n,m,a))
        
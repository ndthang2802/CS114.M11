import math
n = int(input())

def rutGon(a,b):
    u = math.gcd(a,b)
    a //= u
    b //= u
    if b > 1 :
        return str(a) + " " + str(b)
    else :
        return str(a)

for i in range(n):
    a,b = list(map(int,input().split()))
    print(rutGon(a,b))
n,m = list(input().split())

def solve1(n,m):
    n = int(n)
    m = int(m)
    tg, t10 = n, 1

    while tg > 0:
        tg //= 10
        t10 *= 10

    print(m // t10 + (m % t10 >= n))

def solve2(n,m):
    ln = len(n)
    lm = len(m)

    if(lm == ln) :
        if int(n) > int(m):
            return 0
        else:
            return 1
    elif ln > lm:
        return 0

    else:
        count = 1
        x = int(m[-ln:])
        if x >= int(n):
            for i in range(0,lm - ln):
                t = int(m[-ln-1-i])
                count += t*(10**i)
        else:
            for i in range(0,lm - ln):
                t = int(m[-ln-1-i])
                count += t*(10**i) - 1
            count+=i
        return count
solve1(n,m)
print(solve2(n,m))
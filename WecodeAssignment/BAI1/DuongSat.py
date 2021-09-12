k,t = list(map(int,input().split()));

def solve(k,t):
    r = t // k
    tg = t % k
    if (r % 2 == 0):
        return tg 
    else:
        return k - tg
print(solve(k,t))
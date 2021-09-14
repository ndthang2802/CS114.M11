n = int(input())


for i in range(n):
    q = int(input())
    p = list(map(int,input().split()))

    s = sum(p) / q
    if s != round(s):
        s+=1
    print(int(s))
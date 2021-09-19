



n,m = list(map(int,input().split()))
r,c = list(map(int,input().split()))

arr = []

for i in range(n):
    arr.append(list(input().split()))


if n*m == r*c:
    newarry = []
    for l in arr:
        newarry += l
    x = 0
    for i in range(r):
        print(*newarry[x:x+c])
        x+=c
else:
    for i in range(n):
        print(*arr[i])

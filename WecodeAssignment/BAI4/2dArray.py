
r,c = list(map(int,input().split()))

array = []

col_leng = [0]*c

for i in range(r):
    x = list(map(int,input().split()))
    array.append(x)
    col_leng = [col_leng[j] if col_leng[j] > len(str(x[j])) else len(str(x[j])) for j in range(c)]
for i in range(r):
    a = [str(array[i][j]).rjust(col_leng[j]) for j in range(c)]
    print(*a, end='\n')


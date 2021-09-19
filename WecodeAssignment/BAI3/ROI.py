h,w = list(map(int,input().split()))

img = []
img2 = []

for i in range(h):
    img.append(list(input().split()))
    img2.append([0]*w)
top , left , bottom, right = list(map(int,input().split()))

for i in range(top,bottom+1):
    for j in range(left,right+1):
        img2[i][j] = img[i][j]

for i in range(h):
    print(*img2[i])
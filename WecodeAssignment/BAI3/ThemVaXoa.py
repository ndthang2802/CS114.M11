import sys
state = 0
arr = []
while state != 6:
    a = list(map(int,sys.stdin.readline().split()))
    state = a[0]
    if state == 0:
        if len(arr) != 0:
            arr.insert(0,a[1])
        else:
            arr.append(a[1])
    elif state==1:
        arr.append(a[1])
    elif state==2 and len(arr):
        try :
            i = arr.index(a[1])
            arr.insert(i+1,a[2])
        except:
             arr = [a[2]] + arr
    elif state==3 and len(arr):
        try:
            arr.remove(a[1])
        except:
            pass
    elif state==4 and len(arr):
        try:
            while True:
                arr.remove(a[1])
        except:
            pass
    elif state==5 and len(arr):
        del arr[0]
if len(arr):
    print(*arr)
else:
    print("blank")
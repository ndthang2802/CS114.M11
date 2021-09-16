def ThaoTac() :
    
    state = 0

    arr = []

    while state != 6:
        a = list(map(int,input().split()))
        state = a[0]
        if state == 0:
            arr = [a[1]] + arr
        elif state==1:
            arr.append(a[1])
        elif state==2:
            try :
                i = arr.index(a[1])
                arr = arr[:i+1] + [a[2]] + arr[i+1:]
            except:
                 arr = [a[2]] + arr
        elif state==3:
            try:
                i = arr.index(a[1])
                arr = arr[:i] + arr[i+1:]
            except:
                pass
        elif state==4:
            try:
                while True:
                    arr.remove(a[1])
            except:
                pass
        elif state==5:
            arr = arr[1:]
    if len(arr):
        print(*arr)
    else:
        print("blank")
ThaoTac()
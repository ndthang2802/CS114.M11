n = int(input())

arr = list(map(int,(input().split())))


k , target = list(map(int,(input().split())))

def ps(arr,target):
    sum = 0
    for i in range(len(arr)):
        sum+= abs(arr[i]-target)
    return sum


def TimKsoGanNhat(arr,k,target):
    if target <= arr[0]:
        return arr[:k]
    elif target >= arr[-1]:
        return arr[(-1)*k:]
    else :
        temp = ps(arr[:k],target);
        start = 0
        end = k
        t = abs(arr[0] - target)
        for i in range(1,len(arr)-k):
            new_temp = temp - t + abs(arr[i+k-1] - target)
            t = abs(arr[i] - target)
            if new_temp >= temp:
                return arr[start:end]
            else:
                temp = new_temp
                start = i
                end = i+k
        return arr[start:end]




print(*TimKsoGanNhat(arr,k,target))
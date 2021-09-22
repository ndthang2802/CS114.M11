import sys
import bisect
from collections import deque
n = int(input())

arr = list(map(int,sys.stdin.readline().split()))

def ps(arr,target):
    sum = 0
    for i in range(len(arr)):
        sum+= abs(arr[i]-target)
    return sum

def indexOfClosetNumber(arr,target):
    if len(arr) == 1:
        return 0
    i = 0; j = len(arr); mid = 0
    while (i < j):
        mid = (i + j) // 2
 
        if (arr[mid] == target):
            return arr[mid]
 
        if (target < arr[mid]) :
 
            if (mid > 0 and target > arr[mid - 1]):
                if target - arr[mid-1] <= arr[mid] - target:
                    return mid - 1
                else:
                    return mid
            j = mid
        
        else :
            if (mid < len(arr) - 1 and target < arr[mid + 1]):
                if target - arr[mid] >= arr[mid+1] - target:
                    return mid 
                else:
                    return mid + 1
            
            i = mid + 1
    return mid

def TimKsoGanNhat(arr,k,target):
    if target <= arr[0]:
        return (arr[0],arr[k-1])
    elif target >= arr[-1]:
        return (arr[(-1)*k],arr[-1])
    else :
        i = 0
        try:
            i = arr.index(target)
        except:
            i = indexOfClosetNumber(arr,target)
        l = i - 1
        r = i + 1
        c = 1
        #res = deque()
        #res.append(arr[i])
        start = arr[i]
        end = arr[i]
        while c < k:
            if l < 0:
                #res.append(arr[r])
                end = arr[r]
                r+=1
                c+=1             
            elif r == len(arr):
                #res.appendleft(arr[l])
                start = arr[l]
                l-=1
                c+=1
            elif target - arr[l] <= arr[r] - target:
                #res.appendleft(arr[l])
                start = arr[l]
                l -= 1
                c+=1
            else:
                #res.append(arr[r])
                end = arr[r]
                r+=1  
                c+=1
        return (start,end)          
def findNums(a, k, x):
    i = bisect.bisect_left(a, x, 0, len(a) - 1)
    left = max(0, i - k + 1)
    right = left + k - 1
    while (right + 1) < len(a) and a[right + 1] - x < x - a[left]:
        left += 1
        right += 1
    return(a[left], a[right])
while True :
    try:
        k , target = list(map(int,sys.stdin.readline().split()))
        res  = TimKsoGanNhat(arr,k,target)
        print(str(res[0]) + ' ' + str(res[1]))
        print(findNums(arr,k,target))
    except:
        break




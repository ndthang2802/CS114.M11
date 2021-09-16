a,b = list(map(int,input().split()))

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))


def MergeSortedArray(arr1,arr2):

    res = arr1 + arr2
    res.sort()
    return res
print(*MergeSortedArray(arr1,arr2))
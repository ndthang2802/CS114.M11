x = input()

soChuSo = len(x)

def isArmstrongNumber(x):
    sum = 0
    for _ in x :
        sum += int(_)**soChuSo
    return sum == int(x)

print(isArmstrongNumber(x))

test = int(input())


def kiemTra(s,t):
    
    for c in s:
        if c in t:
            return 'YES'
    return 'NO'

for i in range(test):
    s = input()
    t = input()

    print(kiemTra(s,t))
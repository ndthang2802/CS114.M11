x = int(input())

def Fibo(n):
    if n < 1 or n > 30 : 
        return 'So '+ str(n) +' khong nam trong khoang [1,30].'
    t = [];
    if(n == 1):
        return 1
    for i in range(n):
        if len(t) == 0 or len(t) == 1:
            t.append(1)
        else :
            t.append(t[0]+t[1])
            t.pop(0)
    return t[1];

print(Fibo(x))
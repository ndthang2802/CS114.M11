s = input()

t = input()

def checknghichdao(s,t):
    if s == t[::-1]:
        return 'YES'
    else:
        return 'NO'

print(checknghichdao(s,t))
    

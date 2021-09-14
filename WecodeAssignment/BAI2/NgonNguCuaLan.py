import re

s = list(map(str,input().split()))

def isNoun(s):
    Malepattern = r"\D*(etr)$"
    Femailpattern = r"\D*(etra)$"
    if re.match(Malepattern,s):
        return (True,'M')
    elif re.match(Femailpattern,s):
        return (True,'FM')
    return (False,None)

def isAdj(s):
    Malepattern = r"\D*(lios)$"
    Femailpattern = r"\D*(liala)$"
    if re.match(Malepattern,s):
        return (True,'M')
    elif re.match(Femailpattern,s):
        return (True,'FM')
    return (False,None)

def isVerb(s):
    Malepattern = r"\D*(initis)$"
    Femailpattern = r"\D*(inites)$"
    if re.match(Malepattern,s):
        return (True,'M')
    elif re.match(Femailpattern,s):
        return (True,'FM')
    return (False,None)


def check(s):

    next_A_ok = True
    next_N_ok = True
    next_V_ok = False

    flag = ''

    for w in s :
        N = isNoun(w)
        A = isAdj(w)
        V = isVerb(w)

        if N[0]:
            if flag =='':
                flag = N[1]
            else:
                if not flag == N[1]:
                    return False
            if next_N_ok:
                next_A_ok = False
                next_N_ok = False
                next_V_ok = True
            else:
                return 'NO'
        elif A[0]:
            if flag =='':
                flag = A[1]
            else:
                if not flag == A[1]:
                    return False
            if not next_A_ok:
                return 'NO'
        elif V[0]:
            if flag =='':
                flag = V[1]
            else:
                if not flag == V[1]:
                    return False
            if not next_V_ok:
                return 'NO'
        else:
            return 'NO'
    return 'YES'

print(check(s))
        
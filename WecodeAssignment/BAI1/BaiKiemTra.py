n = int(input())
k = int(input())
p = int(input())
q = int(input())


def BobPosition(n,k,p,q):
    if q == 2:
        alice_pos = p*q
    else :
        alice_pos = p*2 - 1
    if alice_pos - k <= 0 and alice_pos + k > n:
        print(-1)
    else :
        if alice_pos - k > 0:
            bob_pos = alice_pos - k
            if bob_pos % 2 == 0:
                print(int(bob_pos/2),2)
            else:
                print(int(bob_pos//2)+1,1)
            
        else:
            bob_pos = alice_pos + k
            if bob_pos % 2 == 0:
                print(int(bob_pos/2),2)
            else:
                print(int(bob_pos//2)+1,1)



BobPosition(n,k,p,q)
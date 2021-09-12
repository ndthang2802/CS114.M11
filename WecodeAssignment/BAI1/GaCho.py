soCon,soChan = list(map(int,input().split()))

def timGaCho(soCon,soChan):
    socho = (soChan - 2*soCon) / 2
    soga = soCon - socho
    return [int(soga),int(socho)] 

print(*timGaCho(soCon,soChan))
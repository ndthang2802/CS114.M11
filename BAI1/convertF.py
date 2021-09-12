from decimal import *
F = float(input())
getcontext().prec = 6
def FtoC(F):
    return (F - 32) / 1.8
    
def FtoK(F):
    return FtoC(F) + 273.15
print(Decimal(FtoC(F)).normalize(),Decimal(FtoK(F)).normalize())

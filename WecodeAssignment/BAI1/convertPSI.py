#prec says how many digits to keep starting from the most significant non-zero digit. So in your result:

from decimal import *
getcontext().prec = 6
n = float(input())
def convertPSI(x):
    a = 0.453592 / (2.54**2)
    return Decimal(x*a).normalize()
print(convertPSI(n))
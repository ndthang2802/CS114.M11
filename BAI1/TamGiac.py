x = float(input())
y = float(input())
z = float(input())

def DienTich(x,y,z):
    p = (x + y + z) / 2
    res = round(pow(p*(p-x)*(p-y)*(p-z),0.5),2)
    if(res == int(res)):
        return int(res)
    else:
        return res

def TamGiac(x,y,z):
    if x + y <= z or x + z <= y or y + z <= x :
        return 'Khong phai tam giac' 
    else :
        if x == y and y == z:
            return 'Tam giac deu, dien tich = ' + str(DienTich(x,y,z)) 
        elif pow(x,2) == pow(y,2) + pow(z,2) or pow(y,2) == pow(x,2) + pow(z,2) or pow(z,2) == pow(y,2) + pow(x,2):
            return 'Tam giac vuong, dien tich = ' + str(DienTich(x,y,z)) 
        elif x == y or x == z or y == z:
            return 'Tam giac can, dien tich = ' + str(DienTich(x,y,z)) 
        else:
            return 'Tam giac thuong, dien tich = ' + str(DienTich(x,y,z)) 

            
print(TamGiac(x,y,z))
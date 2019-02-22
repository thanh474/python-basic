#gan k co gia tri la chuoi
k = "phai la thang bo no"
#in ra man hinh bien k
print(k)
#in ra man hinh kieu du lieu cua k
print(type(k))
#gan gia tri cua bien a =
a=1.3330333033303330333
print(a)
#kieu du lieu cua k in duoc 15 so sau dau cham
print(type(a))

#neu muon lay phan xap xi cao hon 15 thi ta dung kieu deximal
#import thu vien decimal
#lay toan bo noi dung thu vien decimal
#tu thu vien decimal no import nmoi thu vao (*)
from decimal import*


#lay toi da 30 chu so phan nguyen va phan thap phan decimal
#ham nay ko dung cung dc chi lay lon ra ay nho lai
getcontext ().prec =30

#voi cau len nay no chi in ra 15 chu so sau dau cham va lam tron
#no hieu la kieu float 
f =10 /3
print(f)
#voi cau lenh nay no in ra 30 chu so sau phan thap phan 
d=Decimal(10)/Decimal(3)
print (d)

#chi mot thang la decimal chi so nguyen no van ra ket qua la so thu
p = 10 / Decimal(3)
print(p)
print(type(p))


#phan so dung ham Fraction
from fractions import*
q= Fraction(6,9)
print(q) 
print(type(q)) 
q1 = Fraction(1,8)
q3 = q1 +q
print(q3)

#cac phuong thuc bien doi chuoi 
#phuong thuc capitalize
#tac dung tra ra chuoi co ky tu dau viet hoa
#con lai la viet thuong	
q ='ccccai nay Hay Gheccc'
qq = q.capitalize()
print(q)
print(qq)
#cach goi ten ham va thuoc tinh trong mot class 
#ta viet bien do roi vit dau cham roi ten ham
#vd pp = p. capitalize()
# voi upper ra ket qua viet hoa
qqq = q.upper()
print(qqq)

#voi lower
qqqq = q.lower()
print(qqqq)
 
#phuong thuc swapcase
#chuyn nguoc nhau 2 chu hoa >thuong va ng lai
qqqqq = q.swapcase()
print(qqqqq)

#tra ve mot chuoi co chu cai dau tien cua chu vie hoa
#ham title
q1=q.title()
print(q1)

#phuon thuc center can giua
#2 = q.center(width,[fillchar])
#width chua ra 30 o de hien thi can giua
#fillchar cac khoang 
q2 = q.center(30,'-')
print(q2)
# can phai
q3 = q.rjust(30,'-')
print(q3)
#can trai 
q4 = q.ljust(30,'-')
print(q4)

#phuong thuc xu ly
#encode ma hoa chuoi
#co the dich giua 2 ngon ngu 
# phai dung theo chuan
q5 = q.encode()
print('1', q5)

#join la cong chuoi va vs nhau
#cong danh sach vao 1 chuoi
q6 = q.join(['1','oi','wow'])
print('2', q6)

# replace la thay the thg nay = thg khac
#neu them cout thi no chi thay the ky tu do 
q7 = q.replace('a','k',0 )
print(q7)

#strip tra ve chuoi ko co ky ty dau va chuoi o 2 dau 
q8 = q.strip('c')
print('3', q8)
#cat trai 
q9 = q.lstrip('c')
print(q9)
#cat phai
q10 = q.rstrip('c')
print(q10)
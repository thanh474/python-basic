#xu ly chuoi
#chuoi tran la gi la chuoi in ra cac gia tri dac biet
#them r vao dau
print (r'haizz, \neauwebu') 

#toan tu cong 
a ='bui'
b ='thanh'
c = a + '\t' + b
print (c)

#toan tu nhan 
d ='bui\t'
e = d*2
print (e)

#toan tu in 
#chi nhan dc 2 dap an la true hoac fale
#kiem tra mot chuoi co nam trong 1 chuoi hay ko
r = 'abcdefghi'
t ='k'
#neu t ton tai trong r thi in ra ket qua dc luu vao p
p = t in r
#neu dung in ra true con sai in ra false
print (p)


#lay gia tri o mot vi tri nao do ta dung 
#goi la ham char
o = r[3]
print(o)
y = r[-3]
print(y)

#truy cap phan tu cuoi cung cua chuoi 
#chuoi bat dau tu phan tu 0 va phan tu n-1
#phan tu 0 la phan tu thu 1 , chuoi co n phan thu thi phan tu cuoi cung la n-1
i = r[len(r)-1]
#ham len dem so thu tu co trong chuoi 
print(i)

#cat chuoi tu trai qua phai
#chuoi r se lay tu vi tri 1 den vi tri 5
q = r[1:5]
print (q)
print(r[-3:len(r)])
w = r[1:None]
print(w)
e =  int('99')
print(e)
a = float("66.09")
print(a)
s = int(9.88)
print(s)
#tu so thanh chuoi 
d = str (99)
print(d )
# them mot ky thu vao chuoi
r = r[None:1] +'0' + r[4:None]
print(r) 
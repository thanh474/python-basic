# kieu list gioi han trong ngoac vuong
#cac phantu trong list cach nhau dau ,
#chua moi kieu du lieu  va chinh no
print('\tlenh1')
a =[1,'r',9.0,[99.00,33],['yebv']]
print(a)

#list 
print('\nlenh 2')
b = [i for i in range (30)]
print(b)
 #list  dun voi cac vong lap
print('\nlenh 3')
c = [[i,i*2,i%2] for i in range(5,10)]
print(c)
print('\nlenh 4')
# tao tung list trong chuoi 
#iterable tap hop cac phan tu
d = list('bui')
print(d)
d1= tuple('thanh')
print(d1)

print('\nlenh 5')
#nhan chuoi len nhieu lan 
q =[1,2,34,9] 
print(q*2)
# doi voi toan tu cong tuong tu
#in kiem tra  8 thg co trong 1 thg hay ko  
print(8 in q)
#w= 8 in q
#print(w)

print('\nlenh 6')
# lay phan tu n trong list a thi trong ngoac lay n-1
# lay ra phan tu trong list cua list a
#e = a[3][1]
#print(e)
print (a[3][0])

print('\nlenh 7')
#lay phan tu thu 1 den 3 cua list a
#r = a[1:4]
print(a[1:3])

print('\nlenh 8')
# thay doi noi dung list 
a[3]= 'thanh'
b1 = a[3]
print(a)

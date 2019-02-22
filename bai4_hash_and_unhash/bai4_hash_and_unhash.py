#hashable 
#gioi thieu ham id
# ket qua tra ve la int or longint 
#gia tri nay ko thay doi suot ct
#la mot dia chi dinh danh trong RAM

a = id(1)	 
print(a)

#no cap vung nho cho ban su dung
b='thanh'
c= id(b)
print(c)
print(id('thanh'))


#toan tu huong doi tuong
#toan tu la phuon thuc
n =69
print(n)

print(n+1)
print(n.__add__(1))# tuong dong tren

print(n-1 )
print('1',n.__sub__(1))

print(n*2)
print(n.__mul__(2))

print(1+n)
print(n.__radd__(1))

#tuong tu vs __rmul__

print(-n)
print(n.__neg__())

#khac biet giua hash va unhash

#xet hash 
s1 = 'bui'
s2 = 'thanh'

print(id(s1))
print(id(s2))
print('\n')
s1 = s1 + "bui"
s2 += 'bui'
print(id(s1))
print(id(s2))
print('\n')
# xet unhash
s3 = [1,2,3]
s4 = [7,8,9]
print('2',id(s3))
print(id(s4))
print('\n')

s3= s3 + [0]    #hash dia chi thay doi
s4 += [0]       # unhash dia chi ko thay doi
print(id(s3))
print(id(s4))
print('\n')
#lam nhu the nay co su thay doi dia chi trg RAM
s5 = [1,2,3]
print(id(s5))
s5 = s5.__add__([3,4])
print(id(s5))
print('\n')

#con lam the nay thi ko thay doi dia chi trong RAM
s6 = [1,2,3]
print(id(s6))
s6.__add__([3,4])
print(id(s6))
print('\n')
#list la mot hash nen neu ban lam cac toan tu thi no thuc hien bt va thay doi cac gia tri
#voi hash ban ko the thay doi noi dung, dia chi cua no
#do do python chi xin du lieu ma no can luu no ko xin thua
#do vay neu thay doi gia tri no ko con cho luu nen no di chuyen sang mot dia chi khac lon hon de co the luu dc
# hash se do ton dung luon nho hon 

#con doi vs unhash thi nguoc lai 
#no xin thua noi dung de luu them 
#tuple la hash nen chiem it dung luong hon nen no nhanh hon list
#thay doi gia tri truc tiep nhu list

#ta xet vd sau 
#doi vs list la unhash
a1 = [ 1,2,3]
a1.append((4,5)) # ham
print(a1)

# doi voi tuple la  hash
a2 = (1,2,3)
a2 += (4,5)  # toan tu
print(a2)
# vi khi dung  tuple thi may phai di tim bo nho cho no
#con list thi khong

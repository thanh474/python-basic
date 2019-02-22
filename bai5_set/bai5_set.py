#set ko phai la unhash
# duoc gioi han {}
# tac ca phan tu tron no la set
#set ko chua nhieu hon 1 phan tu trung lap
#chi chua hash 
# nhung no khong chua unhash
#no khong the tu chua no

s1 ={6,7}
print(s1)

s2 = {(1,2,3),('iqnci')}
print(s2)
# khong the chua set va list ma 2 kieu kia la unhash
# no khong tao set
s3 = {i for i in range(3)}
print(s3)
print(type(s3))

# contruster tao ra set chu ko tao ra list hoac tuple
# tach tung phan tu ra
s4 = set ('bui cong thanh')
print(s4)

#set no khong quan tam den vij tri cac phan tu
#no chi xuat mot gia tri neu no lam nhau
s5 = set([1,2,3,3,4,3,9,3])
print(s5)

# mot so toan tu trong set 
# biru do venn
# toan tu in 
print((5,6) in {1,2,3,(5,6)})

#toan tu tru 
# tra ve ket qua chi ton tai trong set1 ma khong ton tai trong set2
print({1,2,3,'ii'}-{1,2})
#co the tra ra mot set rong
# nho hon tru lon hon tra ra rong

# toan tu va 
# ket qua  tra ve vua tong taij trong set1 vua ton tai trong set2
print({1,2,2,34} & {2,3,4,5})

# toan tu hoac
# tra ra cac gia tri co trong 2 set
#neu co gia tri trung nhau thi chi in ra 1 gia tri
print({1,2,3,4} | {3,4,5,6})


# toan tu so 
print({1,2,3,4} ^ {4,5,6,7})
# tra ca gia tri chi co trong hai set cac phan tu giong nhau khong xuat ra


# indexing va cat thih khong dc ho tro
# cac phuong thuc clear       
# xoa cac phan tu trong set
q1 = {1.3,4,5}
q2 = q1.clear()
print(q2)

# phuon thuc pop 
# ket qua tra ve la ket qua dc lay ra khoi set 
# dong thoi trong set do khong con gia tri do

q3 = {1,2,3,4,5}
print(q3)
q4 = q3.pop() # chi lay ra thang dau tien 
print(q4)

#phuong thuc  remove
print('\n')

q5={1,2,3,4}
q5.remove(4)# remo tu phan tu 0 den phan tu 2
print(q5)

# phuon thuc thuc discard tuong tu remove nhung hay hon 
q6 = {1,2,3,4,6}
q6.discard(9)
print(q6)


# phuong thuc copy
# copy set ra mot ban sao dua no den mot vung nho khac
q7 = {1,2,3,4}
q8 =q7.copy()
q7.remove(4)
print('1' ,q7)
print('2 ',q8)

# phuonng thuc add them mot phan tu vao set
# neu phan tu them cho trong set thi no khong hien thi
# chi dc them mot phan tu
w1 = {1,2,3}
w1.add(4)
print(w1)
#set la unhash 

# cau hoi set
se1 = {1,2,3}
se2 = se1
se2.clear()
print(se2)
print(id(se1))
print(id(se2))

# boi vi se1 va se2 cung tham chieu( chi )toi vung 
#nho  luu gia tri se1 ne khi clear s2 thi vung nho luc do trong
#ma vung nho trong thi se1 kho co gia tri in ra la rong

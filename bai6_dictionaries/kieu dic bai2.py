# cac phuong thuc co tron dict
# phuong thuc copy 
# tac dung la sao chep dict nay ra mot vung nho moi
s1 = {1:1,(1,2):'1928'}
s2 = s1.copy()
print(s2)

# phuong thuc clear xoa toan bo du lieu tron dict

# cac phuong thuc xu ly
# phuong thuc get theo key lay ra value
s3 = {'bui': 'thanh',(1,2,3):'lata'}
s4 = s3.get((1,2,3))
print(s4)
#neu ko co trong dict thi no in ra defaul
s5 = s3.get("naion",'defaul')
print(s5)

#phuong thuc item
# lay ra tra ve 1 gt lop dict la 1 tuple vs gia tri 1 la key 2 laf value
s6 = s3.items()
print(s6)
# neu chuyen thanh list thi no se lay dc tung gia tri mot
s7 = list(s3.items())
print(s7[0][0])
print('1 ',s7[0])

# phuong thuc key 
# lay ra danh sach ten key trong dict nay
s8 = s3.keys()
print(s8)

#phuon thuc value 
# lay ra danh sach cac value tron dict nay ]
s9 = s3.values()
print('danh sach cac valude')
print(s9)


# phuon thuc pop bo di phan tu co key va hien  thi value do 
# trong truong hop ko co key thi no in none
s10 = s3.pop('bui')
print(s10)
print(s3)
# neu ta them defaul thi se ko bi loi
s11 = s3.pop('119','defaul')
print(s11)

# popitem  lay mot ket qua ngau nhien trong dict
# va ket qua lay ra se ko con trong dict
q1 = {'1,2':99,12:'haha','115':115}
s12 = q1.popitem()
print(s12)


#detdefault
# tra ve gia tri cua key 
#th key ko co trong dict thi tra ve gia tri default
# co the them 1 cap value moi va dict

q2 = {1:00, 'bui':'thah'}
q3 = q2.setdefault(1)
print(q3)

# neu ko co thi no them vao dict va co value la none
q4 = q2.setdefault(1999,'haha')
print(q4)
print(q2)

#cap nhat noi dun ten dict
# phuong thuc update 
# them dict 
q2.update(bui='congthanh')
print(q2)
# thay doi cac gia value thay value moi 






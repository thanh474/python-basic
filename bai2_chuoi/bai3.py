#goi la kieu du lieu tuple
#chuyen vao chuoi
thah = ('thanh')
q = 'bui cong %s la super %s' %(thah,'man')
print(q)
w = ('%s cong %s')
ww = w %('bui','thanh')
print(ww)
# %0.5f truyen vao so thuc
#lay 5 so sau dau ,
e = 'so thuc la: %8.3f' 
ee = e %(9.123567)
print(ee)
#%f co the lam tron 
e = 'so thuc la: %8.3f' 
ee = e %(9.49998)
print(ee)
#%d truyen vao so nguyen
r = '%d' %(9)
print(r)
# %r truyen vao gia tri trong phan %
y = '%r' %("bwcn")
print(y)

#tim bien chuyen cho vao chuoi 
#chuoi f
u = 'bui cong'
i = f'{u} thanh'
print(i)
 
name ='bui cong thanh'

phone = '0968692725'

thanh = f'''Student: {name}
Address: {{address}}
Phone: {phone}
Born year: {{boreyear}}  '''
print(thanh)

# dinh dang format gan giong voi dang %
#khong can bien dang gi 
#con cai nay chi can dung thu tu
d = 'a:{} , b:{} , c:{}'.format(9,0.8,1)
print(d)
#cai nay lay theo dung thu tu ma no dc dat trong format
o = 'a:{1} , b:{2} , c:{0}'.format('one',1,9.9)
print(o)
#tuong tu nhung no chi tiet hon
chi = '1:{mot},2:{hai}'.format(mot=99.99,hai=11)
print(chi)
#chung ta cp the su dung no de can le 
#tang tinh tham my ha ha 
#can giua nay
s = '0000{:*^10}99999'.format("1234")
print(s)
#can le trai nay 
left = "{:-<20} ".format('can le trai')
print(left)
#can le phai
right = 'can {:->10} phai'.format("le")
print(right)



# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)
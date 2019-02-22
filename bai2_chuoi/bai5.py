#cac phuong thuc 
#tach chuoi cat chuoi
#split tra ve kieu du lieu lit bang chia phan tu theo
a = 'bui cong thanh'
c= "tao la ai"


print('1',a)

print('2',a.split('n'))

#max split tach so lan dc cung cap

print('3',a.split('n',1))

#cat tu phia ban phai qua

print('4',a.rsplit('n',1))

#partition cat chi phan tu do ra tinh tu trai sang

print('5',a.partition('n'))
# tinh tu phai sang

print('6', a.rpartition('n'))

#phuon thuc count dem ky tu mk cho co trong chuoi

print('7 ',a.count('n'))
#dem thu dau den dau

print('8 ',a.count('n',0,8))
#startswith tra ra 2 gia tri la true or flase
#co phai ban dau ban cai do ko

print('9 ',a.startswith('n'))

print('10 ',a.startswith('n',6,10))

#endwith tuong tu nhung xet tu cuoi chuoi

print('11 ',a.endswith('h'))

#find tim chuoi trong 1 chuoi

print('12 ',a.find('n')
)
# voi r find thi tuong tu
# phuong thuc index giong find neu ko thay ket qua no in ra loi

print('13 ',c.index('o'))

# kiem tra chuoi co phai la so hay ko

print('14 ',a.isdigit())
# isspace tra ve chuoi ma co ky tu trong

print('15 ', b.isspace())
# du lieu dictionary
# dic dung cac key de truy suat cac phan tu
# dic gioi han boi {}
# value co the giong nhau nhung keu thi phai khac nhau
# cac phan tu cua dic phan tach nhau = dau ,
#dic luon di vs nhau mot cap la key va value
#dic la mot hash
ten = {'name':'thanh',23:331}
print(ten)

#co the khoi tao dic rong
# co the su dung comprehension
q1 = {key : value for key , value in [('thanh',12),(99,'bui')]}
print(q1)

#contructer dict
q2 = dict()
print(q2)

# khoi tao mot dict tu mot mapping
# may cai nhu dieu la __add__
# khong phai mapping oj  khong phai luc nao cung la dict oj
# dict oj con co nhieu phuong thuc khac  keys va __getitem__ ma cn nhieu phan tu kha

# khoi tao interable
# no  phai chua 2 value  do chinh la cap key-value
# no tu hieu tuan tu key va value
q3 = [('1','hello'),('thanh', 99)]
q4 = dict (q3)
print(q4)

# khoi taoo keyword arguments 
#khoi tao gia trij roi chuyen cho bien

thanh = "cong"
qben ='hoi'
q4 = dict ( thanh ='bui', qben ='qbnm')
print(q4)

# su dung fromkeys 
# cho phep khoi tao mot dict voi cac key trong mot interable
# cac gia tri nay deu nhan dc gia tri mac dinh la none
#in cac value la none
q5 = ('nam','niu')
qw = ('none')
q6 = dict.fromkeys(q5,qw)
print(q6)

# lay value trong dict bang key
print(ten['name'])
 # thay doi noi dun cua dict bang key
 # dict la mot unhash  ne co the thay doi duoc no giong list
ten ['name']='cong'
print('1', ten)
# neu bao mot key khong co thi no tu dong them key do vao  dict  va in ra
ten['9911']='1199'
print(ten )
print(ten['9911'])

dic = dict(k=13,kk='16')
dic['k'] = dic ['k'] + 1
dic ['kk'] = dic ['kk'] + ' bui thanh'
print(dic)
print(dic['k'])

# them mot phan tu thu cong giong list
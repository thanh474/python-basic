import math
def chuvi(r):
	if r<0:
		print('wrong')
	elif r==0:
		print('wrong')
	else :
		x= 2 * r
		print(x)

def dien(r):
	if r<0:
		print('wrong')
	elif r==0:
		print('wrong')
	else:
		v = 2*math.pi*math.pow(r, 2)
		print(v)

r = float(input("nhap r: "))
dien(r)
chuvi(r)
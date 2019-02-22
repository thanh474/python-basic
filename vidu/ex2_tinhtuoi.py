import time
x= time.localtime()

def tuoi(de):
	a = x[0] - de
	if a == 0 :
		print("tuoi cua ban la: ",a+1)
	elif a<0 :
		print("vo van khong phai tuoi cua ban.")
	else :
		print ("tuoi cua ban la: ", a)

de = int(input("nhap nam sinh cua ban: "))

tuoi(de)
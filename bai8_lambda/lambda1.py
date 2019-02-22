list_goc = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]

list_moi = list(filter(lambda a: (a%2 == 0) , list_goc))

# Kết quả: [10, 8, 6, 2, 4]
# By Quantrimang.com
print(list_moi)
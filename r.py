import random
r = random.randint(1, 100) #.=的 產生隨機數功能1~100
count = 0
while True:
	count += 1 #count = count + 1
	num = input('請猜一個1-100之間的數字: ')
	num = int(num)
	if num == r:
		print('猜中了!這是你猜的第', count , '次')
		break
	elif num > r:
		print('比答案大')
	else:
		print('比答案小')
	print('這是你猜的第', count , '次') #在if架構之外，才不用重複寫
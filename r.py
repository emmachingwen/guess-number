import random
r = random.randint(1, 100) #.=的 產生隨機數功能1~100

while True:
	num = input('請猜一個1-100之間的數字: ')
	num = int(num)
	if num == r:
		print('猜中了!')
		break
	elif num > r:
		print('比答案大')
	else:
		print('比答案小')
x = 0
x = int(x)
while x < 3:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		x = 5
	else:
		y = 2 - x
		print('密碼錯誤，你還有', y ,'次機會')
		x = x + 1
if x == 3:
	print('錯誤過多，已封鎖')
else:
	print('密碼正確')
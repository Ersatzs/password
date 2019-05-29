password = 'a123456'
i = 3
while True:
	pwd = input('请输入您的密码：')
	if pwd == password:
		print('登入成功！')
		break
	else:
		i = i - 1
		print ('密码错误')
		if i > 0:
			print('还有', i ,'次机会')
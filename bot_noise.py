# 函数功能:检测复读。2代表这是第三位复读者，1代表这是第四位以上复读者，0代表其余情况
def check(i, list_n, num, content):
	t = 0
	if not content:
		list_n[i] = 'message_test'
		num[i] = 0
	elif num[i] == 0:
		list_n[i] = content
		num[i] = num[i] + 1
	elif num[i] < 100:
		if list_n[i] == content:
			num[i] = num[i] + 1
		else:
			list_n[i] = content
			num[i] = 1
		if num[i] == 3:
			t = 2
		if num[i] > 3:
			t = 1
	return (list_n, num, t)
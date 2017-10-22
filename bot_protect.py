# 保护系统
import bot_IOfile


# 函数功能:输入保护列表、保护使用次数列表、成员QQ号,执行添加操作,输出新的列表和回馈文本
def add(list_p, limit, qq):
	if qq in list_p:
		msg = '您已经在保护列表中,无需重复添加'
	else:
		for i in range(len(limit)):
			if qq == limit[i]["qq"]:
				if limit[i]["limit"] == 0:
					msg = '今日保护指令次数已用完'
				else:
					limit[i]["limit"] = limit[i]["limit"] - 1
					list_p.append(qq)
					success = bot_IOfile.write_pkl_data(list_p, 'D:\Python POJ\lxybot\data\data_protect_list.pkl')
					if success == 1:
						msg = '设置成功!进入保护模式'
					else:
						msg = '本地保存失败,请联系dalou,错误代码:11'
				return list_p, limit, msg
		limit.append({"qq": qq, "limit": 1})
		list_p.append(qq)
		success = bot_IOfile.write_pkl_data(list_p, 'D:\Python POJ\lxybot\data\data_protect_list.pkl')
		if success == 1:
			msg = '设置成功!进入保护模式'
		else:
			msg = '本地保存失败,请联系dalou,错误代码:12'
	return list_p, limit, msg


# 函数功能:输入保护列表、成员QQ号，执行移除操作,输出新的保护列表和回馈文本
def sub(list_p, qq):
	if qq in list_p:
		t = list_p.index(qq)
		del list_p[t]
		success = bot_IOfile.write_pkl_data(list_p, 'D:\Python POJ\lxybot\data\data_protect_list.pkl')
		if success == 1:
			msg = '解除成功!可以干坏事了'
		else:
			msg = '本地保存失败,请联系dalou,错误代码:13'
	else:
		msg = '你压根就不是无敌的!'
	return list_p, msg

# 健康系统的添加和去除功能
import bot_IOfile


# 函数功能: 输入关爱列表、成员QQ号,执行添加操作,输出新的关爱列表和回馈文本
def add(list_h, qq):
	if qq in list_h:
		msg = '您已经是关爱对象了,无需重复添加\n输入!care查看'
	else:
		list_h.append(qq)
		success = bot_IOfile.write_pkl_data(list_h, 'D:\Python POJ\lxybot\data\data_health_list.pkl')
		if success == 1:
			msg = '设置成功!dalou将会每晚关照您的健康\n输入!care查看'
		else:
			msg = '本地保存失败,请联系dalou,错误代码:21'
	return list_h, msg


# 函数功能: 输入关爱列表、成员QQ号,执行移除操作,输出新的关爱列表和回馈文本
def sub(list_h, qq):
	if qq in list_h:
		t = list_h.index(qq)
		del list_h[t]
		success = bot_IOfile.write_pkl_data(list_h, 'D:\Python POJ\lxybot\data\data_health_list.pkl')
		if success == 1:
			msg = '移除关爱对象成功\n输入!care查看'
		else:
			msg = '本地保存失败,请联系dalou,错误代码:22'
	else:
		msg = 'dalou压根就没在关心你!'
	return list_h, msg

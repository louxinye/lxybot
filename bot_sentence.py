# 判决系统,执行禁言和踢人
from qqbot import _bot as bot


# 函数功能:群号、成员qq号、禁言时间,执行禁言操作
def shut(group, member, smoke):
	gl = bot.List('group', group)
	if gl:
		group1 = gl[0]
		member1 = bot.List(group1, member)
		if member1:
			bot.GroupShut(group1, member1, smoke)
			msg = '操作执行完毕(若对方为群主或者管理员则不会生效)'
		else:
			msg = '失败:找不到此人信息!'
	else:
		msg = '失败:找不到群组信息!'
	return msg


# 函数功能:群号、成员qq号,执行踢人操作
def kick(group, member):
	gl = bot.List('group', group)
	if gl:
		group1 = gl[0]
		member1 = bot.List(group1, member)
		if member1:
			bot.GroupKick(group1, member1)
			msg = '踢人操作执行完毕(若对方为群主或者管理员则不会生效)'
		else:
			msg = '踢人失败:找不到此人信息!'
	else:
		msg = '踢人失败:找不到群组信息!'
	return msg

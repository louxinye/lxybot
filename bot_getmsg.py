# 函数功能:查看各类帮助文档或者列表


def help():
	txt = '''发烟bot使用说明

!group  查看适用群
!sorry  发超星图主动认错
!rest   1小时休息套餐
!sleep  6小时睡眠套餐
!afk    闭群套餐(可选参数)
!remove 私聊解禁(限好友)
!repeat 复读(需要参数)
!roll   随机取数(可选参数)
!true   随机测谎(需要参数)
!kill   查询机票获得者
!健康系统
!保护系统
!地雷系统
!手雷系统
!复读系统
!监视系统
!咩羊游戏
!egg   查询对话彩蛋
!dog   查询bot权限者

v1.50 正式版'''
	return txt


def noise():
	txt = '''复读惩罚系统介绍

此系统开启或者关闭需要权限
开启后效果:
1.当同一句话被连续发送3次,bot会立刻成为第四位复读者
2.bot自动复读之后,凡是继续复读的成员立刻被禁言10分钟
3.拥有保护状态的成员禁言时间将会减少至1分钟
4.图片不会被计入复读,同时也会打断当前复读内容'''
	return txt


def health():
	txt = '''健康系统介绍

☆!health: 加入健康套餐列表中
☆!stop_h: 将自己从健康套餐列表中移除
☆!care: 查询健康套餐名单
套餐效果:
1.每天凌晨0-8点时期如果在群内发言,将直接禁言至8点
2.拥有保护状态的玩家不受影响'''
	return txt


def protect():
	txt = '''保护系统介绍

☆!defense: 加入保护列表中,每天只允许成功使用2次
☆!stop_d: 将自己从保护列表中移除
☆!protect: 查询保护名单
保护效果:
1.任何彩蛋对话都不会触发
2.复读惩罚时间减少为1分钟
3.健康监督功能失效
4.呜喵群中不受地雷和手雷影响,但同时禁止攻击'''
	return txt


def bomb():
	txt = '''地雷系统介绍

此全部功能仅呜喵群有效
☆埋地雷: 设置一个地雷(15%失败,禁言1分钟)
☆埋一堆地雷: 随机设置2-100个地雷(25%失败,禁言3分钟)
☆拆地雷: 拆掉一个地雷(25%失败,禁言3分钟,但是地雷数仍然会少1)
☆踩地雷: 强行使自己中雷(50%成功,禁言10分钟,此时地雷数少1)
☆普通中雷: 除去bot能识别的语句(例如!各类指令,彩蛋等)外,5%中雷,禁言1分钟
【提醒】埋雷有风险,若当前地雷数≥14个,再埋雷将有(埋雷前地雷数+1)%的概率地雷大爆炸,禁言30分钟。处于保护状态成员将无法使用本系统'''
	return txt


def diu():
	txt = '''手雷系统介绍

此全部功能仅呜喵群有效
指令分为两种,但效果一样:
☆丢手雷@某群员: 该指令要求必须艾特变蓝色,且对方群名片没有奇怪的符号
☆丢手雷@某群员的qq号 : 该指令要求艾特不变色(相当于手打了个qq号),但是最后要加一个空格
使用效果:75%成功,对方禁言1分钟;25%失败,自己禁言3分钟
【提醒】若保护系统触发,会强制改变成功率'''
	return txt


def mie():
	txt = '''1+1游戏介绍

bot算法由咩羊提供
☆!game: 开始游戏,可选难度(缺省值2)
☆!stop_g: 强制结束游戏
难度说明:
1 教学级
2 大神级
3 噩梦级
4 怀疑人生级
5 退群删游戏级
游戏介绍:
你和bot各拥有两个数字, 双方轮流行动, 每方取出自己一个数去加对面的一个数, 如果和大于10则减去10, 直到某一方的两个数字均为0则获胜。游戏过程中数字0不得作为加或者被加的对象, 这点请注意。
操作方法:
正确输入格式为:x y, 其中x是你的其中一只手的数字, y是bot其中一只手的数字, 且均取值1~9之间'''
	return txt


def jian():
	txt = '''监视系统介绍

☆!set_bp: 加入监视列表中(需要参数, 第一个参数为你的用户名; 第二个参数为mode, 缺省值0; 两个参数间用半角逗号隔开)
☆!reset_bp: 从监视列表中移除(参数同上)
☆!bp: 查询监视名单
使用举例:
!set_bp Aero-zero,3
监视效果:
1.当用户刷新了bp前20，则会全群通知
2.当用户倒刷了一张原本为bp前20的图，则会全群通知
【提醒】只对500pp以上的玩家生效。此功能对bot的资源占用相当大, 请尽量保持监视列表不超过20个(当前上限30人)。全群通知会有几分钟的延迟。
后续会有优化计划，争取能同时支持100人的监视
'''
	return txt


def killL(list_k):
	msg = '即将被踢的人名单如下:\n'
	for user in list_k:
		msg = msg + '群号%s 成员%s 剩余时间%s\n' % (user["group"], user["qq"], user["time"])
	msg = msg + '上述成员将会在时间结束后得到一张飞机票'
	return msg


def careL(list_h):
	msg = '健康套餐名单如下(QQ号)\n'
	for user in list_h:
		msg = msg + '%s\n' % user
	msg = msg + '想查询健康内容请输入!健康系统'
	return msg


def eggL(list_e):
	msg = '一共有10个隐藏对话彩蛋,已经得到:\n'
	for i in range(0, 10):
		if list_e[i] == 1:
			msg = msg + '%s号\n' % (i + 1)
	msg = msg + '注:彩蛋每天需要重新解锁一次\n解锁最后一个彩蛋者请带截图私聊dalou,发放一个月撒泼特,该活动永久有效直到产生得奖者'
	return msg


def protectL(list_p):
	msg = '保护列表如下(QQ号)\n'
	for user in list_p:
		msg = msg + '%s\n' % user
	msg = msg + '想查询保护内容请输入!保护系统'
	return msg


def dogL(list_g, list_d):
	msg = '权限者列表如下(QQ号)\n神级别:\n'
	for user in list_g:
		msg = msg + '%s\n' % user
	msg = msg + '正常级别:\n'
	for user in list_d:
		msg = msg + '%s\n' % user
	msg = msg + '【注1】在一般群员基础上,权限者多拥有下列指令:\n!noise  !stop_n\n!kill@  !stop_k@\n!smoke@  !unsmoke@\n埋满地雷  清除地雷\n'\
				'【注2】同时还有下列变动:\n休息、睡眠、闭群指令失效\n不会普通中地雷\n不会被他人丢手雷'
	return msg


def bpL(list_b):
	msg = ''
	std_msg = ''
	taiko_msg = ''
	ctb_msg = ''
	mania_msg = ''
	for user in list_b:
		if user[20]["user_mode"] == '0':
			std_msg = std_msg + '%s\n' % user[20]["user_name"]
		if user[20]["user_mode"] == '1':
			taiko_msg = taiko_msg + '%s\n' % user[20]["user_name"]
		if user[20]["user_mode"] == '2':
			ctb_msg = ctb_msg + '%s\n' % user[20]["user_name"]
		if user[20]["user_mode"] == '3':
			mania_msg = mania_msg + '%s\n' % user[20]["user_name"]
	if std_msg:
		msg = msg + '【std】\n%s' % std_msg
	if taiko_msg:
		msg = msg + '【taiko】\n%s' % taiko_msg
	if ctb_msg:
		msg = msg + '【ctb】\n%s' % ctb_msg
	if mania_msg:
		msg = msg + '【mania】\n%s' % mania_msg
	if not msg:
		msg = 'bot没有对任何人进行bp监视'
	else:
		msg = '监视列表如下:\n'+ msg + '用户id仅供参考(不排除有人改名)。上述成员更新bp将会进行实时通知'
	return msg

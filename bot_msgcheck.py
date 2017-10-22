# 带有参数的部分指令检查系统
import random
import re
import bot_sentence
from qqbot import _bot as bot


# 函数功能:!afk指令检查
def afk(group, member, content):
	if content == '!afk':
		msg = bot_sentence.shut(group, member, 86400)
	elif '!afk ' in content:
		check_num = re.match(r'!afk ([123456789][0123456789]*)', content)
		if check_num:
			ban_day = int(check_num.group(1))
			if ban_day >= 30:
				smoke = 2591940
			else:
				smoke = ban_day * 86400
			msg = bot_sentence.shut(group, member, smoke)
		else:
			msg = '您的!afk指令使用错误'
	else:
		msg = '无法识别,bot猜测您是想使用指令!afk x(x为参数,缺省值1)'
	return msg


# 函数功能:!roll指令检查
def roll(content):
	if content == '!roll':
		num = random.randint(1, 100)
		msg = 'roll了一个%s' % num
	elif '!roll ' in content:
		check_roll = re.match(r'!roll ([123456789][0123456789]*)', content)
		if check_roll:
			roll_max = int(check_roll.group(1))
			if roll_max > 100000:
				msg = '参数过大'
			else:
				num = random.randint(1, roll_max)
				msg = 'roll了一个%s' % num
		else:
			msg = '您的!roll指令使用错误'
	else:
		msg = '无法识别,bot猜测您是想使用指令!roll x(x为参数,缺省值100)'
	return msg


# 函数功能:!true指令检查
def true(content):
	if content == '!true':
		msg = '您的!true指令使用错误'
	elif '!true ' in content:
		check_true = re.match(r'!true (.*)', content)
		if check_true:
			success = random.randint(1, 2)
			if success == 1:
				msg = '您说的对'
			else:
				msg = '您说错了'
		else:
			msg = '您的!true指令使用错误'
	else:
		msg = '无法识别,bot猜测您是想使用指令!true x(x为参数)'
	return msg


# 函数功能:!repeat指令检查
def repeat(content):
	if content == '!repeat':
		msg = '你说了啥'
	elif '!repeat ' in content:
		check_repeat = re.match(r'!repeat (.*)', content)
		if check_repeat:
			msg = check_repeat.group(1)
			if '!' in msg:
				msg = '为了bot的安全,请不要在复读内容中添加半角感叹号'
		else:
			msg = '您的!repeat指令使用错误'
		if not msg:
			msg = '你说了啥'
	else:
		msg = '无法识别,bot猜测您是想使用指令!repeat x(x为参数)'
	return msg


# 函数功能:!egg指令检查
def egg(list_e, content):
	check_egg = re.match(r'!egg ([123456789][0123456789]*)', content)
	if check_egg:
		i = int(check_egg.group(1))
		if i < 11 and list_e[i-1] == 0:
			list_e[i-1] = 1
			msg = '解锁%s号彩蛋' % i
		else:
			msg = '此彩蛋不存在或者已经解锁'
	else:
		msg = '您的!egg指令使用错误'
	return list_e, msg


# 函数功能:!kill指令检查
def kill(list_k, list_g, list_d,  group, content):
	success = 1
	check_user = re.match(r'!kill@(.*) ', content)
	if check_user:
		card = check_user.group(1)
		gl = bot.List('group', group)
		if gl:
			group1 = gl[0]
			member1 = bot.List(group1, card)
			if member1:
				for i in range(len(list_k)):
					if group == list_k[i]["group"] and member1[0].qq == list_k[i]["qq"]:
						success = 0
						break
				if member1[0].qq in list_g or member1[0].qq in list_d:
					msg = '你在搞笑吗'
				elif success == 1:
					list_k.append({"group": group, "qq": member1[0].qq, "time": 60})
					msg = '已获得飞机票,现在进入60分钟遗言时间'
				else:
					msg = '这人已经有机票了'
			else:
				msg = '找不到此人信息'
		else:
			msg = '找不到群组信息'
	else:
		msg = '您的!kill指令使用错误'
	return list_k, msg


# 函数功能:!stop_k指令检查
def stop_k(list_k, group, content):
	success = 0
	check_user = re.match(r'!stop_k@(.*) ', content)
	if check_user:
		card = check_user.group(1)
		gl = bot.List('group', group)
		if gl:
			group1 = gl[0]
			member1 = bot.List(group1, card)
			if member1:
				for i in range(len(list_k)):
					if group == list_k[i]["group"] and member1[0].qq == list_k[i]["qq"]:
						del list_k[i]
						success = 1
						break
				if success == 0:
					msg = '这人并没有机票'
				else:
					msg = '已经取消此人的机票'
			else:
				msg = '找不到此人信息'
		else:
			msg = 'bot遇到了奇怪的错误!'
	else:
		msg = '您的!stop_k指令使用错误'
	return list_k, msg


# 函数功能:!remove指令检查
def remove(list_g, member, content):
	msg = '本功能暂时关闭'
	'''
	if content == '!remove':
		msg = '您的!remove指令使用错误,格式应当如下\n!remove 群代码(1主群,2分群,3贫民窟)\n举例: !remove 1'
	elif '!remove ' in content:
		check_num = re.match(r'!remove ([123])', content)
		if check_num:
			num = int(check_num.group(1)) - 1
			group_id = list_g[num]
			msg = bot_sentence.shut(group_id, member, 0)
		else:
			msg = '您的!remove指令使用错误,格式应当如下\n!remove 群代码(1主群,2分群,3贫民窟)\n举例: !remove 1'
	else:
		msg = '无法识别,bot猜测您是想使用指令!remove x(x为参数)'
	'''
	return msg


# 超星图惩罚指令
def smoke(list_g, group, content):
	check_user = re.match(r'!smoke@(.*) ', content)
	if check_user:
		card = check_user.group(1)
		gl = bot.List('group', group)
		if gl:
			group1 = gl[0]
			member1 = bot.List(group1, card)
			if member1:
				if member1[0].qq in list_g:
					msg = '你在搞笑吗'
				else:
					boom = random.randint(1, 100)
					msg = bot_sentence.shut(group, member1[0].qq, boom * 60)
			else:
				msg = '找不到此人信息'
		else:
			msg = '找不到群组信息'
	else:
		msg = '您的!smoke指令使用错误'
	return msg


# 解禁指令
def unsmoke(group, content):
	check_user = re.match(r'!unsmoke@(.*) ', content)
	if check_user:
		card = check_user.group(1)
		gl = bot.List('group', group)
		if gl:
			group1 = gl[0]
			member1 = bot.List(group1, card)
			if member1:
				msg = bot_sentence.shut(group, member1[0].qq, 0)
			else:
				msg = '找不到此人信息'
		else:
			msg = '找不到群组信息'
	else:
		msg = '您的!unsmoke指令使用错误'
	return msg


# 函数功能:!game指令检查
def game(game_content, game_member, member_qq, content):
	if content == '!game':
		if game_member:
			level_max = 0
			msg = '该游戏正在被玩家%s占用,若要停止则需要本人使用!stop_g' % game_member
		else:
			level_max = 4
			game_member = member_qq
			msg = '锁定玩家成功!\n难度: 大神级\nbot目前数字:1 1\n玩家目前数字:1 1'
			game_content = [[1, 1], [1, 1]]
	elif '!game ' in content:
		if game_member:
			level_max = 0
			msg = '该游戏正在被玩家%s占用,若要停止则需要本人使用!stop_g' % game_member
		else:
			(level_max, name) = game_diff(content)
			if level_max > 0:
				game_member = member_qq
				msg = '锁定玩家成功!\n难度: %s\nbot目前数字:1 1\n玩家目前数字:1 1' % name
				game_content = [[1, 1], [1, 1]]
			else:
				msg = '难度输入有误'
	else:
		level_max = 0
		msg = '无法识别,bot猜测您是想使用指令!game x(x为参数,缺省值2)'
	return game_content, game_member, msg, level_max


def game_diff(content):
	check_game = re.match(r'!game [12345]', content)
	if check_game:
		t = int(content[6])
		if t == 1:
			level_max = 2
			diff_name = '教学级'
		elif t == 2:
			level_max = 3
			diff_name = '大神级'
		elif t == 3:
			level_max = 4
			diff_name = '噩梦级'
		elif t == 4:
			level_max = 6
			diff_name = '怀疑人生级'
		elif t == 5:
			level_max = 8
			diff_name = '退群删游戏级'
		else:
			level_max = 0
			diff_name = '???级'
	else:
		level_max = 0
		diff_name = '???级'
	return level_max, diff_name
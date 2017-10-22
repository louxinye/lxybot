# 地雷与手雷系统
import re
import random
import bot_sentence
from qqbot import _bot as bot


bomb_group = '326389728'


# 丢手雷
def diu(list_d, list_p, assassin_qq, content):
	global bomb_group
	check_diu = re.match(r'丢手雷@(.*) ', content)
	if check_diu:
		card = check_diu.group(1)
		gl = bot.List('group', bomb_group)
		if gl:
			group1 = gl[0]
			member1 = bot.List(group1, card)
			if member1:
				if assassin_qq in list_p:
					bot_sentence.shut(bomb_group, assassin_qq, 180)
					msg = '你踏马还想干坏事!'
				elif member1[0].qq in list_d:
					bot_sentence.shut(bomb_group, assassin_qq, 180)
					msg = '居然敢丢权限汪!'
				elif member1[0].qq in list_p:
					bot_sentence.shut(bomb_group, assassin_qq, 180)
					msg = '对方处于保护状态!'
				else:
					success = random.randint(1, 100)
					if success < 76:
						bot_sentence.shut(bomb_group, member1[0], 60)
						msg = '对方成功被炸伤!'
					else:
						bot_sentence.shut(bomb_group, assassin_qq, 180)
						msg = '小手一抖原地自爆!'
			else:
				msg = '完全无法理解你要炸谁!'
		else:
			msg = '群组信息获取失败!'
	else:
		msg = '您的丢手雷指令使用错误'
	return msg


# 埋地雷
def set_one(list_p, assassin_qq, bomb):
	global bomb_group
	if assassin_qq in list_p:
		msg = '你踏马还想干坏事!'
	else:
		success = random.randint(1, 100)
		if success < 16:
			bot_sentence.shut(bomb_group, assassin_qq, 60)
			msg = '埋雷过程中误爆,被炸伤!'
		elif bomb > 13:
			boom = random.randint(1, 100)
			if boom < bomb + 2:
				bot_sentence.shut(bomb_group, assassin_qq, 1800)
				msg = '地雷大爆炸!当前还有0个雷'
				bomb = 0
			else:
				bomb = bomb + 1
				msg = '埋雷成功,当前还有%s个地雷!' % bomb
		else:
			bomb = bomb + 1
			msg = '埋雷成功,当前还有%s个地雷!' % bomb
	return msg, bomb
			
			
# 埋一堆地雷
def set_many(list_p, assassin_qq, bomb):
	global bomb_group
	if assassin_qq in list_p:
		msg = '你踏马还想干坏事!'
	else:
		success = random.randint(1, 100)
		number = set_bomb()
		if success < 26:
			bot_sentence.shut(bomb_group, assassin_qq, 180)
			msg = '埋雷过程中误爆,被炸伤!'
		elif bomb > 13:
			boom = random.randint(1, 100)
			if boom < bomb + 2:
				bot_sentence.shut(bomb_group, assassin_qq, 1800)
				msg = '地雷大爆炸!当前还有0个雷'
				bomb = 0
			else:
				bomb = bomb + number
				msg = '埋一堆雷成功(%s个),当前还有%s个地雷!' % (number, bomb)
		else:
			bomb = bomb + number
			msg = '埋一堆雷成功(%s个),当前还有%s个地雷!' % (number, bomb)
	return msg, bomb


# 拆地雷
def chai(list_p, assassin_qq, bomb):
	global bomb_group
	if assassin_qq in list_p:
		msg = '保护状态无法拆雷!'
	else:
		if bomb > 0:
			bomb = bomb - 1
			success = random.randint(1, 100)
			if success < 76:
				msg = '拆地雷成功,当前还有%s个地雷!' % bomb
			else:
				bot_sentence.shut(bomb_group, assassin_qq, 180)
				msg = '拆雷失败爆炸!当前还有%s个地雷!' % bomb
		else:
			msg = '已经没有地雷可以拆了'
	return msg, bomb


# 踩地雷
def cai(list_p, assassin_qq, bomb):
	global bomb_group
	if assassin_qq in list_p:
		msg = '保护状态无法踩雷!'
	else:
		if bomb > 0:
			success = random.randint(1, 100)
			if success < 51:
				bot_sentence.shut(bomb_group, assassin_qq, 600)
				bomb = bomb - 1
				msg = '踩地雷成功!当前还有%s个地雷!' % bomb
			else:
				msg = '踩地雷失败!当前还有%s个地雷!' % bomb
		else:
			msg = '已经没有地雷可以踩了'
	return msg, bomb


# 函数功能:随机输出埋一堆地雷的个数
def set_bomb():
	success_num = random.randint(0, 199)
	if success_num < 1:
		number = 100
	elif success_num < 3:
		number = 50
	elif success_num < 5:
		number = 25
	elif success_num < 8:
		number = 15
	elif success_num < 12:
		number = 12
	elif success_num < 16:
		number = 10
	elif success_num < 20:
		number = 8
	elif success_num < 40:
		number = 7
	elif success_num < 60:
		number = 6
	elif success_num < 100:
		number = 5
	elif success_num < 140:
		number = 4
	elif success_num < 180:
		number = 3
	else:
		number = 2
	return number

# -*- coding: utf-8 -*-
import random
import time
import bot_sentence
import bot_IOfile
import bot_health
import bot_protect
import bot_noise
import bot_bomb
import bot_msgcheck
import bot_game
import bot_get
import bot_osu
from qqbot import qqbotsched

group_list = ['614892339', '514661057', '326389728']  # 适用群组列表
god_list = ['3059841053']  # 绝对权限者的qq号
dog_list = ['77808542', '873743955', '630060047', '2541721178', '1719583076', '1773805744']  # 普通权限者的qq号
repeat_num = [100, 100, 100]  # 当前复读次数, 若大于等于100则表示没有开启复读惩罚。和适用群一一对应。
repeat_list = ['message_test', 'message_test', 'message_test']  # 当前正在被复读的话。和适用群一一对应。
egg_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 彩蛋列表, 被解锁则置1
bomb = 0  # 地雷数量
allow_bomb = 2  # 允许使用地雷和手雷系统的群代号。需要和适用群对应。
protect_limit = []  # 保护系统使用次数列表, 里面每个元素代表一个用户。每个用户组成为[qq号, 还可以使用的次数]
game_member = ''  # 正在使用咩羊游戏的玩家qq号
game_content = [[1, 1], [1, 1]]  # 咩羊游戏初始值
game_diff = 0  # 咩羊游戏难度
kill_list = []  # 即将被踢的人列表, 里面的每个元素由[群号，qq号，剩余时间]组成
# 恢复关爱列表、保护列表、bp监视列表
health_list = bot_IOfile.read_pkl_data('D:\Python POJ\lxybot\data\data_health_list.pkl')
protect_list = bot_IOfile.read_pkl_data('D:\Python POJ\lxybot\data\data_protect_list.pkl')
user_bp_list = bot_IOfile.read_pkl_data('D:\Python POJ\lxybot\data\data_bp_care_list.pkl')
# 初始化每个人保护系统的使用次数
for protect_i in range(len(protect_list)):
	protect_member_qq = protect_list[protect_i]
	protect_limit.append([protect_member_qq, 2])


def onQQMessage(bot, contact, member, content):
	global bomb
	global game_member
	global game_content
	global game_diff
	global health_list
	global protect_list
	global user_bp_list
	global protect_limit
	global repeat_list
	global repeat_num
	global kill_list
	global egg_list
	# 任意群聊或私聊通用指令
	# 测试响应指令
	if content == '!hello':
		bot.SendTo(contact, '响应测试成功')
	# 查看帮助指令!help
	elif content == '!help':
		msg = bot_get.help()
		bot.SendTo(contact, msg)
	# 查看适用群指令!group
	elif content == '!group':
		msg = 'bot的功能仅在下列群适用\n'
		for group in group_list:
			msg = msg + '%s\n' % group
		msg = msg + '群代码从上往下依次记为1,2,3,4,私聊解除禁言时候会用到。'
		bot.SendTo(contact, msg)

	# 仅限适用群的通用指令
	elif contact.ctype == 'group' and contact.qq in group_list and member.qq != '1061566571':
		group_i = group_list.index(contact.qq)
		egg_unlock = 0
		# 查看地雷相关指令!地雷系统
		if content == '!地雷系统':
			msg = bot_get.bomb()
			bot.SendTo(contact, msg)
		# 查看手雷相关指令!手雷系统
		elif content == '!手雷系统':
			msg = bot_get.diu()
			bot.SendTo(contact, msg)
		# 查看免疫相关指令!免疫系统
		elif content == '!保护系统':
			msg = bot_get.protect()
			bot.SendTo(contact, msg)
		# 查看健康相关指令!健康系统
		elif content == '!健康系统':
			msg = bot_get.health()
			bot.SendTo(contact, msg)
		# 查看复读相关指令!复读系统
		elif content == '!复读系统':
			msg = bot_get.noise()
			bot.SendTo(contact, msg)
		# 查看监视相关指令!监视系统
		elif content == '!监视系统':
			msg = bot_get.jian()
			bot.SendTo(contact, msg)
		# 查看小游戏相关指令!咩羊游戏
		elif content == '!咩羊游戏':
			msg = bot_get.mie()
			bot.SendTo(contact, msg)
		# 查看踢人列表指令!kill
		elif content == '!kill':
			msg = bot_get.killL(kill_list)
			bot.SendTo(contact, msg)
		# 查看关爱列表指令!care
		elif content == '!care':
			msg = bot_get.careL(health_list)
			bot.SendTo(contact, msg)
		# 查看已经得到的彩蛋指令!egg
		elif content == '!egg':
			msg = bot_get.eggL(egg_list)
			bot.SendTo(contact, msg)
		# 查看无敌列表指令!protect
		elif content == '!protect':
			msg = bot_get.protectL(protect_list)
			bot.SendTo(contact, msg)
		# 查看狗管理指令!dog
		elif content == '!dog':
			msg = bot_get.dogL(god_list, dog_list)
			bot.SendTo(contact, msg)
		# 查看bp监视列表指令!bp
		elif content == '!bp':
			msg = bot_get.bpL(user_bp_list)
			bot.SendTo(contact, msg)
		# 复读指令!repeat
		elif '!repeat' in content:
			msg = bot_msgcheck.repeat(content)
			bot.SendTo(contact, msg)
		# 随机取数指令!roll
		elif '!roll' in content:
			msg = bot_msgcheck.roll(content)
			bot.SendTo(contact, msg)
		# 随机测谎指令!true
		elif '!true' in content:
			msg = bot_msgcheck.true(content)
			bot.SendTo(contact, msg)
		# 健康监督指令!health
		elif content == '!health':
			(health_list, msg) = bot_health.add(health_list, member.qq)
			bot.SendTo(contact, msg)
		# 取消健康监督指令!stop_h
		elif content == '!stop_h':
			(health_list, msg) = bot_health.sub(health_list, member.qq)
			bot.SendTo(contact, msg)
		# 地雷和手雷系统
		elif content == '埋地雷' and group_i == allow_bomb:
			(msg, bomb) = bot_bomb.set_one(protect_list, member.qq, bomb)
			bot.SendTo(contact, msg)
		elif content == '埋一堆地雷' and group_i == allow_bomb:
			(msg, bomb) = bot_bomb.set_many(protect_list, member.qq, bomb)
			bot.SendTo(contact, msg)
		elif content == '拆地雷' and group_i == allow_bomb:
			(msg, bomb) = bot_bomb.chai(protect_list, member.qq, bomb)
			bot.SendTo(contact, msg)
		elif content == '踩地雷' and group_i == allow_bomb:
			(msg, bomb) = bot_bomb.cai(protect_list, member.qq, bomb)
			bot.SendTo(contact, msg)
		elif '丢手雷@' in content and group_i == allow_bomb:
			msg = bot_bomb.diu(dog_list, protect_list, member.qq, content)
			bot.SendTo(contact, msg)
		# 加入保护列表指令!defense
		elif content == '!defense':
			(protect_list, protect_limit, msg) = bot_protect.add(protect_list, protect_limit, member.qq)
			bot.SendTo(contact, msg)
		# 移除保护列表指令!stop_d
		elif content == '!stop_d':
			(protect_list, msg) = bot_protect.sub(protect_list, member.qq)
			bot.SendTo(contact, msg)
		# 超星禁言指令!sorry
		elif content == '!sorry':
			smoke = random.randint(1, 60) * 60
			msg = bot_sentence.shut(contact.qq, member.qq, smoke)
			bot.SendTo(contact, msg)
		# bp更新提醒指令!set_bp
		elif '!set_bp' in content:
			(user_bp_list, msg) = bot_osu.set_id(user_bp_list, content)
			# msg = '此功能优化中，暂时关闭'
			bot.SendTo(contact, msg)
		# bp更新提醒指令!reset_bp
		elif '!reset_bp' in content:
			(user_bp_list, msg) = bot_osu.stop_set_id(user_bp_list, content)
			# msg = '此功能优化中，暂时关闭'
			bot.SendTo(contact, msg)
		# 游戏指令!game
		elif '!game' in content:
			(game_content, game_member, msg, diff) = bot_msgcheck.game(game_content, game_member, member.qq, content)
			if diff > 0:
				game_diff = diff
			bot.SendTo(contact, msg)
		# 结束游戏指令!stop_g
		elif content == '!stop_g':
			if member.qq == game_member:
				game_diff = 0
				game_member = ''
				msg = '解除成功,游戏结束'
			else:
				msg = '您并没有绑定该游戏'
			bot.SendTo(contact, msg)
		# 几个彩蛋回复
		elif 'no limit' in content and member.qq not in protect_list:
			msg = '这图过时了,dalou现在推荐洪水!'
			bot.SendTo(contact, msg)
			if egg_list[0] == 0:
				egg_list[0] = 1
				bot.SendTo(contact, '解锁1号彩蛋')
				egg_unlock = 1
		elif '解锁2号彩蛋' in content and member.qq not in protect_list:
			msg = '我草'
			bot.SendTo(contact, msg)
			if egg_list[1] == 0:
				egg_list[1] = 1
				bot.SendTo(contact, '解锁2号彩蛋')
				egg_unlock = 1
		elif '培养晶体' in content and member.qq not in protect_list:
			msg = '化学式都不认识?'
			bot.SendTo(contact, msg)
			if egg_list[2] == 0:
				egg_list[2] = 1
				bot.SendTo(contact, '解锁3号彩蛋')
				egg_unlock = 1
		elif '指甲盖' in content and member.qq not in protect_list:
			msg = '有人要加入指甲盖映射吗?'
			bot.SendTo(contact, msg)
			if egg_list[3] == 0:
				egg_list[3] = 1
				bot.SendTo(contact, '解锁4号彩蛋')
				egg_unlock = 1
		elif ('daloubot队' in content or 'DalouBot队' in content) and member.qq not in protect_list:
			msg = '这么垃圾的队名,不如公平正义队!'
			bot.SendTo(contact, msg)
			if egg_list[4] == 0:
				egg_list[4] = 1
				bot.SendTo(contact, '解锁5号彩蛋')
				egg_unlock = 1
		elif 'dalou不在' in content and member.qq not in protect_list:
			msg = '然而bot在!虽然没啥用'
			bot.SendTo(contact, msg)
			if egg_list[5] == 0:
				egg_list[5] = 1
				bot.SendTo(contact, '解锁6号彩蛋')
				egg_unlock = 1
		elif 'hhhhhhhh' in content and member.qq not in protect_list:
			msg = '这么鬼畜的笑声只有红月干得出来!'
			bot.SendTo(contact, msg)
			if egg_list[6] == 0:
				egg_list[6] = 1
				bot.SendTo(contact, '解锁7号彩蛋')
				egg_unlock = 1
		elif ('debug' in content or '断点' in content or 'error' in content or 'warning' in content) and member.qq not in protect_list:
			msg = '程序员真痛苦!'
			bot.SendTo(contact, msg)
			if egg_list[7] == 0:
				egg_list[7] = 1
				bot.SendTo(contact, '解锁8号彩蛋')
				egg_unlock = 1
		elif '现在是半夜,请睡觉了' in content and member.qq not in protect_list:
			msg = '你也睡觉去吧'
			bot.SendTo(contact, msg)
			if egg_list[8] == 0:
				egg_list[8] = 1
				bot.SendTo(contact, '解锁9号彩蛋')
				egg_unlock = 1
		elif '一身正气' in content and member.qq not in protect_list:
			msg = '没错，都是我干的!'
			bot.SendTo(contact, msg)
			if egg_list[9] == 0:
				egg_list[9] = 1
				bot.SendTo(contact, '解锁10号彩蛋')
				egg_unlock = 1

		# 仅限1+1游戏者使用
		elif member.qq == game_member:
			(game_content, msg1, msg2, gg) = bot_game.one_plus_one_check(game_content, content, game_diff)
			bot.SendTo(contact, msg1)
			if msg2:
				bot.SendTo(contact, msg2)
				if gg == 1:
					game_diff = 0
					game_member = ''
					msg = '解除成功,游戏结束'
					bot.SendTo(contact, msg)

		# 权限指令,狗管理势力登场
		elif member.qq in god_list or member.qq in dog_list:
			# 禁止复读指令!noise
			if content == '!noise':
				if repeat_num[group_i] > 99:
					msg = '复读惩罚开启'
				else:
					msg = '复读惩罚重新启动'
				repeat_num[group_i] = 0
				bot.SendTo(contact, msg)
			# 解除禁止复读指令!stop_n
			elif content == '!stop_n':
				if repeat_num[group_i] < 100:
					msg = '复读惩罚关闭'
				else:
					msg = '复读惩罚已经关闭'
				repeat_num[group_i] = 100
				bot.SendTo(contact, msg)
			# 送飞机票指令!kill
			elif '!kill@' in content:
				(kill_list, msg) = bot_msgcheck.kill(kill_list, god_list, dog_list, contact.qq, content)
				bot.SendTo(contact, msg)
			# 取消送飞机票指令!stop_k
			elif '!stop_k@'in content:
				(kill_list, msg) = bot_msgcheck.stop_k(kill_list, contact.qq, content)
				bot.SendTo(contact, msg)
			# 超星图惩罚指令!smoke
			elif '!smoke@' in content:
				msg = bot_msgcheck.smoke(god_list, contact.qq, content)
				bot.SendTo(contact, msg)
			# 解除禁言指令!unsmoke
			elif '!unsmoke@' in content:
				msg = bot_msgcheck.unsmoke(contact.qq, content)
				bot.SendTo(contact, msg)
			# 分群清除地雷指令!清除地雷
			elif content == '清除地雷' and group_i == allow_bomb:
				bomb = 0
				msg = '地雷全部清除完毕!'
				bot.SendTo(contact, msg)
			# 分群埋满地雷指令!埋满地雷
			elif content == '埋满地雷' and group_i == allow_bomb:
				if bomb > 99:
					msg = '地雷已经满了,下一个埋雷必大爆炸'
				else:
					number = 100 - bomb
					bomb = 100
					msg = '埋一堆雷成功(%s个),当前还有100个地雷!' % number
				bot.SendTo(contact, msg)

			# 然而，有的指令只能神来用
			elif member.qq in god_list:
				# 直接解锁彩蛋指令!egg
				if '!egg ' in content:
					(egg_list, msg) = bot_msgcheck.egg(egg_list, content)
					bot.SendTo(contact, msg)

		# 非权限指令,除权限以外所有群员均适用
		else:
			# 权限功能检测
			if content == '!noise' or content == '!stop_n' or content == '埋满地雷' or content == '清除地雷' or '!kill@' in content or '!smoke@' in content:
				msg = '你没有权限!'
				bot.SendTo(contact, msg)
			# 休息指令!rest
			elif content == '!rest':
				msg = bot_sentence.shut(contact.qq, member.qq, 3600)
				bot.SendTo(contact, msg)
			# 睡眠指令!sleep
			elif content == '!sleep':
				msg = bot_sentence.shut(contact.qq, member.qq, 21600)
				bot.SendTo(contact, msg)
			# 暂时弃坑指令!afk
			elif '!afk' in content:
				msg = bot_msgcheck.afk(contact.qq, member.qq, content)
				bot.SendTo(contact, msg)
			# 分群中地雷
			elif group_i == allow_bomb:
				if bomb > 0:
					success = random.randint(1, 100)
					if success < 6:
						bomb = bomb - 1
						if member.qq in protect_list:
							msg = '成功躲过一次地雷爆炸!当前还有%s个地雷!' % bomb
						else:
							bot_sentence.shut(contact.qq, member.qq, 60)
							msg = '中雷啦!当前还有%s个地雷!' % bomb
						bot.SendTo(contact, msg)
		# 复读惩罚
		if repeat_num[group_i] < 100:
			(repeat_list, repeat_num, t) = bot_noise.check(group_i, repeat_list, repeat_num, content)
			if t == 1:
				if member.qq in protect_list:
					bot_sentence.shut(contact.qq, member.qq, 60)
				else:
					bot_sentence.shut(contact.qq, member.qq, 600)
				msg = '求求你别复读了'
				bot.SendTo(contact, msg)
			if t == 2:
				msg = content
				bot.SendTo(contact, msg)
		# 健康监督触发
		if member.qq in health_list and member.qq not in protect_list:
			t_hour = int(time.strftime('%H', time.localtime(time.time())))
			t_minute = int(time.strftime('%M', time.localtime(time.time())))
			if 0 <= t_hour <= 7:
				smoke = 8 * 60 * 60 - t_hour * 60 * 60 - t_minute * 60
				bot_sentence.shut(contact.qq, member.qq, smoke)
				msg = '现在是半夜,请睡觉了'
				bot.SendTo(contact, msg)
		# 全彩蛋解锁检查
		if egg_unlock == 1:
			t = 1
			for i in range(0, 10):
				if egg_list[i] == 0:
					t = 0
					break
			if t == 1:
				msg = '全彩蛋解锁!恭喜QQ号%s得到撒泼特1个月' % member.qq
				bot.SendTo(contact, msg)
	# 仅限私聊的指令
	elif contact.ctype == 'buddy' and contact.qq != '1061566571':
		# 解除禁言指令!remove
		if '!remove' in content:
			msg = bot_msgcheck.remove(group_list, contact.qq, content)
			bot.SendTo(contact, msg)


# 定时任务:每过1分钟,将kill_list中所有成员的剩余时间-1,若减到0则执行踢人操作
@qqbotsched(minute='0-59/1')
def kill_task(bot):
	member_num = len(kill_list)
	if member_num > 0:
		for i in range(member_num-1, -1, -1):
			kill_list[i][2] = kill_list[i][2] - 1
			if kill_list[i][2] == 0:
				g1 = bot.List('group', kill_list[i][0])
				if g1:
					msg = bot_sentence.kick(kill_list[i][0], kill_list[i][1])
					bot.SendTo(g1[0], msg)
				del kill_list[i]


@qqbotsched(minute='0-59/6')
def bp_check(bot):
	for num in range(len(user_bp_list)):
		user = user_bp_list[num]
		osu_id = user[20]["user_id"]
		osu_mode = user[20]["user_mode"]
		mode_name = bot_osu.get_mode(osu_mode)
		new_bp = bot_osu.get_bp(osu_id, osu_mode)
		if new_bp:
			for i in range(0, 20):
				if new_bp[i] != user[i]:
					msg = 'bp%s有变化' % (i+1)
					if float(user[i]["pp"]) > float(new_bp[i]["pp"]):
						user_name = bot_osu.get_name(osu_id)
						map_id = user[i]["beatmap_id"]
						map_info = bot_osu.get_map(map_id, osu_mode)
						mod = bot_osu.get_mod(user[i]["enabled_mods"])
						old_pp = float(user[i]["pp"])
						new_pp = float(bot_osu.get_map_pp(osu_id, map_id, osu_mode))
						if user_name and map_info and new_pp:
							msg = '%s倒刷了一张图 (%s)\n被倒刷的谱面bid:%s\n%s\nMod: %s\n倒刷前的pp:%.2f\n现在的pp:%.2f' % (user_name, mode_name, map_id, map_info, mod, old_pp, new_pp)
							new_bp.append({"user_id": osu_id, "user_name": user_name, "user_mode": osu_mode})
							user_bp_list[num] = new_bp
							bot_IOfile.write_pkl_data(user_bp_list, 'D:\Python POJ\lxybot\data\data_bp_care_list.pkl')
					else:
						user_name = bot_osu.get_name(osu_id)
						map_id = new_bp[i]["beatmap_id"]
						map_info = bot_osu.get_map(map_id, osu_mode)
						rank = bot_osu.get_rank(new_bp[i]["rank"])
						acc = bot_osu.get_acc(new_bp[i]["count300"], new_bp[i]["count100"], new_bp[i]["count50"], new_bp[i]["countmiss"])
						mod = bot_osu.get_mod(new_bp[i]["enabled_mods"])
						pp = float(new_bp[i]["pp"])
						if user_name and map_info:
							msg = '%s更新了bp%s (%s)\n谱面bid: %s\n%s\n评分: %s\nAcc: %s%%\nMod: %s\npp: %.2f' % (user_name, i+1, mode_name, map_id, map_info, rank, acc, mod, pp)
							new_bp.append({"user_id": osu_id, "user_name": user_name, "user_mode": osu_mode})
							user_bp_list[num] = new_bp
							bot_IOfile.write_pkl_data(user_bp_list, 'D:\Python POJ\lxybot\data\data_bp_care_list.pkl')
					for group in group_list:
						g1 = bot.List('group', group)
						if g1:
							bot.SendTo(g1[0], msg)
					break

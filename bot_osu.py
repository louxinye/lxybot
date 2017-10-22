import requests
import json
import re
import bot_IOfile

osu_api_key = '7f2f84a280917690158a6ea1f7a72b7e8374fbf9'
bp_list = []


def set_id(list_b, content):
	if len(list_b) > 29:
		msg = '达到30人上限!再加的话bot可能会炸,请谅解'
	elif content == '!set_bp':
		msg = '倒是告诉我id啊'
	elif '!set_bp ' in content:
		check_id = re.match(r'!set_bp (.*),([0123])', content)
		if check_id:
			osu_name = check_id.group(1)
			osu_mode = check_id.group(2)
		else:
			check_id = re.match(r'!set_bp (.*)', content)
			if check_id:
				osu_name = check_id.group(1)
				osu_mode = '0'
			else:
				msg = '您的!set_bp指令使用错误'
				return list_b, msg
		(osu_id, pp, real_name) = get_id(osu_name, osu_mode)
		if not osu_id:
			msg = '查不到这个人哎'
		elif pp < 300:
			msg = '该号pp较低, 不进行监视'
		else:
			success = 1
			for user in list_b:
				if user[20]["user_id"] == osu_id and user[20]["user_mode"] == osu_mode:
					success = 0
					break
			if success == 1:
				bp_msg = get_bp(osu_id, osu_mode)
				if len(bp_msg) == 20:
					user_msg = {"user_id": osu_id, "user_name": real_name, "user_mode": osu_mode}
					bp_msg.append(user_msg)
					list_b.append(bp_msg)
					write_success = bot_IOfile.write_pkl_data(list_b, 'D:\Python POJ\lxybot\data\data_bp_care_list.pkl')
					if write_success == 1:
						msg = '添加bp监视成功!'
					else:
						msg = '本地保存失败,请联系dalou,错误代码:31'
				else:
					msg = 'bp数量低于20个,不进行监视'
			else:
				msg = '已经存在此id,无需重复添加'
	else:
		msg = '无法识别,bot猜测您是想使用指令!set_bp x(x为参数)'
	return list_b, msg


def stop_set_id(list_b, content):
	if content == '!reset_bp':
		msg = '倒是告诉我id啊'
	elif '!reset_bp ' in content:
		check_id = re.match(r'!reset_bp (.*),([0123])', content)
		if check_id:
			osu_name = check_id.group(1)
			osu_mode = check_id.group(2)
		else:
			check_id = re.match(r'!reset_bp (.*)', content)
			if check_id:
				osu_name = check_id.group(1)
				osu_mode = '0'
			else:
				msg = '您的!reset_bp指令使用错误'
				return list_b, msg
		(osu_id, pp, real_name) = get_id(osu_name, osu_mode)
		if not osu_id:
			msg = '查不到这个人哎'
		else:
			success = 0
			bp_num = len(list_b)
			for i in range(0, bp_num):
				if list_b[i][20]["user_id"] == osu_id and list_b[i][20]["user_mode"] == osu_mode:
					success = 1
					del list_b[i]
					break
			if success == 1:
				write_success = bot_IOfile.write_pkl_data(list_b, 'D:\Python POJ\lxybot\data\data_bp_care_list.pkl')
				if write_success == 1:
					msg = '移除bp监视成功!'
				else:
					msg = '本地保存失败,请联系dalou,错误代码:32'
			else:
				msg = '此人并没在监视列表中'
	else:
		msg = '无法识别,bot猜测您是想使用指令!reset_bp x(x为参数)'
	return list_b, msg


# 输入用户名，输出uid和pp和确切的用户名
def get_id(osu_name, osu_mode):
	url = 'https://osu.ppy.sh/api/get_user?k=%s&u=%s&type=string&m=%s&limit=1' % (osu_api_key, osu_name, osu_mode)
	res = get_url(url)
	if not res:
		return 0, 0, 0
	result = json.loads(res.text)
	if len(result) == 0:
		return 0, 0, 0
	else:
		uid = result[0]["user_id"]
		if not result[0]["pp_raw"]:
			result[0]["pp_raw"] = '0'
		pp = float(result[0]["pp_raw"])
		name = result[0]["username"]
		return uid, pp, name


# 输入uid，输出用户名
def get_name(osu_id):
	url = 'https://osu.ppy.sh/api/get_user?k=%s&u=%s&type=id&limit=1' % (osu_api_key, osu_id)
	res = get_url(url)
	if not res:
		return 0
	result = json.loads(res.text)
	if len(result) == 0:
		return 0
	else:
		name = result[0]["username"]
		return name


# 输入uid，输出bp前20
def get_bp(osu_id, osu_mode):
	url = 'https://osu.ppy.sh/api/get_user_best?k=%s&u=%s&type=id&m=%s&limit=20' % (osu_api_key, osu_id, osu_mode)
	res = get_url(url)
	if not res:
		return 0
	result = json.loads(res.text)
	if len(result) == 0:
		return 0
	else:
		return result


# 输入bid，输出图的名字和难度
def get_map(bid, mode):
	url = 'https://osu.ppy.sh/api/get_beatmaps?k=%s&b=%s&m=%s&limit=1' % (osu_api_key, bid, mode)
	res = get_url(url)
	if not res:
		return 0
	result = json.loads(res.text)
	if len(result) == 0:
		msg = '谱面不存在'
	else:
		msg = '%s - %s [%s]\n难度: %.2f (未计算mod)'\
			% (result[0]["artist"], result[0]["title"], result[0]["version"], float(result[0]["difficultyrating"]))
	return msg


# 输入uid，bid，输出此人打这图的pp
def get_map_pp(uid, bid, mode):
	url = 'https://osu.ppy.sh/api/get_scores?k=%s&b=%s&u=%s&type=id&m=%s&limit=1' % (osu_api_key, bid, uid, mode)
	res = get_url(url)
	if not res:
		return 0
	result = json.loads(res.text)
	if len(result) == 0:
		return 0
	else:
		pp = result[0]["pp"]
		return pp


# request请求
def get_url(url, timeout=3):
	try:
		res = requests.get(url, timeout=timeout)
		return res
	except requests.exceptions.RequestException:
		return 0


# 评分转化
def get_rank(content):
	if content == 'X' or content == 'XH':
		msg = 'SS'
	elif content == 'SH':
		msg = 'S'
	else:
		msg = content
	return msg


# acc计算
def get_acc(num_33, num_22, num_11, num_00):
	num_300 = int(num_33)
	num_100 = int(num_22)
	num_50 = int(num_11)
	num_0 = int(num_00)
	total = 6 * (num_300 + num_100 + num_50 + num_0)
	real = 6 * num_300 + 2 * num_100 + num_50
	if total > 0:
		acc = real / total
		msg = '%.2f' % (acc * 100)
	else:
		msg = '???'
	return msg


# mod计算
def get_mod(mod_id):
	mod = int(mod_id)
	mod_list = ['NF','EZ','','HD','HR','SD','DT','RL','HT','NC','FL','AT','SO','AP','PF','4K','5K','6K','7K','8K','FI','RD','LM','','9K','10K','1K','2K','3K']
	choose = []
	msg = ''
	for i in range(28, -1, -1):
		if mod >= 2**i:
			choose.append(mod_list[i])
			mod = mod - 2**i
			if mod_list[i] == 'NC':
				mod = mod - 64
			if mod_list[i] == 'PF':
				mod = mod - 32
	num = len(choose)
	first = 1
	for i in range(num-1, -1, -1):
		if first == 1:
			msg = msg + '%s' % choose[i]
			first = 0
		else:
			msg = msg + ', %s' % choose[i]
	if not msg:
		msg = 'None'
	return msg


# 打印mode
def get_mode(mode_id):
	if mode_id == '0':
		msg = 'std'
	elif mode_id == '1':
		msg = 'taiko'
	elif mode_id == '2':
		msg = 'ctb'
	elif mode_id == '3':
		msg = 'mania'
	else:
		msg = 'unknown mode'
	return msg

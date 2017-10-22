# debug时候用，查看bp监视列表是否出错，一般用于人工纠错
import bot_IOfile


user_bp_list = bot_IOfile.read_pkl_data('D:\Python POJ\lxybot\data\data_bp_care_list.pkl')
num = len(user_bp_list)
print(num)
for i in range(0, num):
	if len(user_bp_list[i]) == 21:
		msg = '%s,%s,%s,%s' % (i, user_bp_list[i][20]["user_id"], user_bp_list[i][20]["user_name"], user_bp_list[i][20]["user_mode"])
	else:
		msg = '这人数据出现异常!'
	print(msg)

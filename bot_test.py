import bot_IOfile


user_bp_list = bot_IOfile.read_pkl_data('D:\Python POJ\lxybot\data\data_bp_care_list.pkl')
num = len(user_bp_list)
print(num)
for i in range(0, num):
	if len(user_bp_list[i]) == 21:
		msg = '%s,%s,%s,%s' % (i, user_bp_list[i][20]["user_id"], user_bp_list[i][20]["user_name"], user_bp_list[i][20]["user_mode"])
	else:
		msg = '这傻逼没bp20!'
	print(msg)
# write_success = bot_IOfile.write_pkl_data(user_bp_list, 'D:\Python POJ\lxybot\data\data_bp_care_list.pkl')
# if write_success == 1:
# 	print('success')
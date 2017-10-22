# 本地文件IO操作
import pickle


# 函数功能:输入数据、文件名,执行写入文件操作
def write_pkl_data(pkl_data, pkl_name):
	try:
		output = open(pkl_name, 'wb')
		pickle.dump(pkl_data, output)
	except IOError:
		return 0
	else:
		output.close()
		return 1


# 函数功能:输入文件名,执行读出文件操作
def read_pkl_data(pkl_name):
	try:
		pkl_file = open(pkl_name, 'rb')
		pkl_data = pickle.load(pkl_file)
	except IOError:
		return []
	else:
		pkl_file.close()
		return pkl_data

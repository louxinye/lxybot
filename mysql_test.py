# -*- coding: utf-8 -*-
import pymysql


db = pymysql.connect("localhost", "root", "123456", "osu")
cursor = db.cursor()
sql = "SELECT * FROM user"
try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		member_qq = row[0]
		print(member_qq)
except ValueError:
	print("error")
db.close()

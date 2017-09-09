#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time
import pymysql
import json

def select_mysql_version():
	# 打开数据库连接
	db = pymysql.connect("localhost", "root", "cqtddt@2016", "test")

	# 使用 cursor() 方法创建一个游标对象 cursor
	cursor = db.cursor()

	# 使用 execute()  方法执行 SQL 查询
	cursor.execute("SELECT VERSION()")

	# 使用 fetchone() 方法获取单条数据.
	data = cursor.fetchone()

	print("Database version : %s " % data)

	# 关闭数据库连接
	db.close()
	return data


def create_mysql_table():
	# 打开数据库连接
	db = pymysql.connect("localhost", "root", "cqtddt@2016", "test")

	# 使用 cursor() 方法创建一个游标对象 cursor
	cursor = db.cursor()

	# 使用 execute() 方法执行 SQL，如果表存在则删除
	cursor.execute("DROP TABLE IF EXISTS JOKE")

	# 使用预处理语句创建表
	sql = """CREATE TABLE JOKE (JOKE_ID BIGINT primary key AUTO_INCREMENT  NOT NULL ,JOKE_NET_SITE  CHAR(50),JOKE_CONTENT TEXT,JOKE_DATE CHAR(20)) DEFAULT CHARSET=utf8"""

	cursor.execute(sql)
	# 关闭数据库连接
	db.close()


def insert_mysql_data():

	title = '/jokehtml/bxnn/201709072307052.htm'
	content = '''小时候家里养条狗，特别通人性，每次上学的时候送我，放学的时候，它都是在村口等我。我上中学了，离家远了，一个星期只能回家一次了。有次课间休息的时候，门卫大爷走进教室给我说，你家的狗来找你了。我惊讶的说：你怎么知道是我家的。门卫大爷看了看我说：它叼着你的照片。。'''
	# 打开数据库连接
	db = pymysql.connect("localhost", "root", "cqtddt@2016", "test")
	db.set_charset('utf8')
	# 使用cursor()方法获取操作游标
	cursor = db.cursor()
	#cursor.execute('')
	datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

	# SQL 插入语句
	sql = """INSERT INTO JOKE(JOKE_NET_SITE,JOKE_CONTENT, JOKE_DATE) VALUES ('%s', '%s', '%s') """
	try:
		# 执行sql语句
		cursor.execute(sql %(title,content,datetime))
		# 提交到数据库执行
		db.commit()
		print("success")
	except:
	 	# 如果发生错误则回滚
	 	db.rollback()
	 	print("fail")
	# 关闭数据库连接
	db.close()


def delete_mysql_data():
	# 打开数据库连接
	db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

	# 使用cursor()方法获取操作游标
	cursor = db.cursor()

	# SQL 删除语句
	sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
	try:
		# 执行SQL语句
		cursor.execute(sql)
		# 提交修改
		db.commit()
	except:
		# 发生错误时回滚
		db.rollback()

	# 关闭连接
	db.close()

def update_mysql_data():
	# 打开数据库连接
	db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

	# 使用cursor()方法获取操作游标
	cursor = db.cursor()

	# SQL 更新语句
	sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')


	try:
		# 执行SQL语句
		cursor.execute(sql)
		# 提交到数据库执行
		db.commit()
	except:
		# 发生错误时回滚
		db.rollback()

	# 关闭数据库连接
	db.close()


def query_mysql_data():
	joke_data = {}
	# 打开数据库连接
	db = pymysql.connect("localhost", "root", "cqtddt@2016", "test")
	db.set_charset('utf8')
	# 使用cursor()方法获取操作游标
	cursor = db.cursor()

	# SQL 查询语句
	sql = "SELECT * FROM JOKE"
	try:
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		results = cursor.fetchall()
		for row in results:
			joke_id = row[0]
			joke_data['id'] = joke_id
			joke_site = row[1]
			joke_data['site'] = joke_site
			joke_content = row[2]
			joke_data['content'] = joke_content
			joke_date = row[3]
			joke_data['date'] = joke_date
			# 打印结果
			print("id=%d,site=%s,content=%s,date=%s" % \
			      (joke_id, joke_site, joke_content, joke_date))
	except:
		print("Error: unable to fetch data")

	# 关闭数据库连接
	db.close()
	print(joke_data)
	return  joke_data


if __name__ == '__main__':


	# 当前时间
	print(time.time())
	# 时间戳形式
	print(time.localtime(time.time()))
	# 简单可读形式
	print(time.asctime(time.localtime(time.time())))
	# 格式化成2016-03-20 11:45:39形式
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

	version = select_mysql_version()

	print("Database mysql : %s " % version)

	create_mysql_table()
	insert_mysql_data()
	joke = query_mysql_data()
	joke_json = json.dumps(joke,ensure_ascii=False)
	print(joke_json)
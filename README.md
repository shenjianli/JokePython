# JokePython

http://www.xxhh.com/page/5/

http://www.jokeji.cn/list.htm

Todo
http://docs.jinkan.org/docs/flask/quickstart.html#web

1.写入数据库
2.python返回json字符串

1.安装Flask
http://www.cnblogs.com/fanglijiao/p/6970678.html

2.


Todo
向数据库中记录上一次请求的site地址，为下一次请求做准备



使用：

jerry@JerrydeMacBook-Pro ~ % mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 17
Server version: 8.0.27 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.02 sec)

mysql> create database joke;
Query OK, 1 row affected (0.01 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| joke               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)

修改数据库root 密码

执行 JokeDb.py  UpdateDB.py
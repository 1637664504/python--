import sqlite3

#连接数据库
con = sqlite3.connect("upload_info.db")

#创建游标示例
cursor = con.cursor()

#执行SQL语句
data = cursor.execute(f'SELECT json_text FROM upload_result WHERE status=\'NEED_UPLOAD\' ORDER BY time ASC;')

#查询并显示数据
#全部显示
item = data.fetchall()

#提交
con.commit()

#关闭数据库连接和游标
cursor.close()
con.close()
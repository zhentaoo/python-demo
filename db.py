import pymysql


conn = pymysql.connect(
    host='127.0.0.1',  # 连接ip
    port=3306,  # 端口号
    user='xxx',  # 数据库用户名
    passwd='xxx',  # 数据库密码
    db='xxx',  # 数据库名
    charset='utf8'  # 设置了数据库的字符集
)

mycursor = conn.cursor()
mycursor.execute("SELECT * FROM eco_bpm_file LIMIT 1")
result = mycursor.fetchone()
print(result)


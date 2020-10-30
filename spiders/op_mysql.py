import config.db_config as dbconfig
import pymysql

db = pymysql.connect(**dbconfig.mysql)
cursor = db.cursor()
# sql = 'select * from stu_score where score = %s'
# res = cursor.execute(sql, (30,))
# print(cursor.fetchone())

sql = "INSERT INTO stu_score(course, stu_name, score) values(%s, %s, %s)"
try:
    cursor.execute(sql, ('ww', 'sde', 90))
    db.commit()
except:
    db.rollback()
db.close()

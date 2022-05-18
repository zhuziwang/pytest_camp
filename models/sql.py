import pymysql

class py_mysql():
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        database='mapping',
        charset='utf8'
    )
    def mysql(self,sql=None):

        cursor = py_mysql.db.cursor()
        cursor.execute(sql)
        data=cursor.fetchone()
        # print(data)
        # cursor.close()

        return data



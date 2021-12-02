import pymysql

class py_mysql():
    db = pymysql.connect(
        host='',
        port=3306,
        user='',
        password='',
        database='',
        charset='utf8'
    )
    def mysql(self,sql=None):

        cursor = py_mysql.db.cursor()
        cursor.execute(sql)
        data=cursor.fetchone()
        print(data)
        # cursor.close()

        return data

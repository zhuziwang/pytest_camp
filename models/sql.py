import pymysql


class PyMysql:
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        database='mapping',
        charset='utf8'
    )

    @staticmethod
    def mysql(sql=None):

        cursor = PyMysql.db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        # print(data)
        # cursor.close()

        return data



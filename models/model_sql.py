import pymysql
'''
把取出的数据格式转换为list，以数据库为存储关键字与用例的地址
'''


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
        data = cursor.fetchall()

        return data

    @staticmethod
    def case(sql=None):
        cursor = PyMysql.db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        list_data = list(data)
        data = []
        for i in range(0, len(list_data)):
            list_data_tuple = list(list_data[i])
            data.append(list_data_tuple)

        i = 0
        l_data = len(data)
        while i < l_data:
            for i in range(0, l_data):
                len_data_data = len(data[i])
                a = 4
                for x in range(4, len_data_data):
                    if a <= len_data_data and ((data[i][a] is None) or (data[i][a] == '')):
                        del data[i][a]
                    else:
                        a += 1
            i += 1
        cursor.close()

        return data


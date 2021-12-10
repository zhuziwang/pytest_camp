import pymysql
'''
把取出的数据格式转换为list，以数据库为存储关键字与用例的地址
'''
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
        data=cursor.fetchall()
        list_data = list(data)
        data = []
        for i in range(0,len(list_data)):
            list_data_tuple=list(list_data[i])
            data.append(list_data_tuple)

        print(data)
        cursor.close()
        return data




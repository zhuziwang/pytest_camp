import pymysql

class py_mysql():
    db = pymysql.connect(
        host='rm-bp11mrw3jq29nkekt.mysql.rds.aliyuncs.com',
        port=3306,
        user='test_group',
        password='0a3HFPCWINZo',
        database='kouyu100_mapping_202000820',
        charset='utf8'
    )
    def mysql(self,sql=None):

        cursor = py_mysql.db.cursor()
        cursor.execute(sql)
        data=cursor.fetchone()
        print(data)
        # cursor.close()

        return data

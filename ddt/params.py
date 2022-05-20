from common.cls.public import CommonPublic
CommonPublic = CommonPublic()


def excel_params():
    from models.model_excel import sheet_to_list
    table_sheet = sheet_to_list("lib/cases/测试用例.xlsx")
    CommonPublic.log(table_sheet)
    return table_sheet


def app_excel_params():
    from models.model_excel import sheet_to_list
    app_table_sheet = sheet_to_list("lib/appcase/测试用例.xlsx")
    CommonPublic.log(app_table_sheet)
    return app_table_sheet


def demo_sql_params(table):
    from models.model_sql import py_mysql
    py_mysql = py_mysql()
    sql1 = "select title,step,method,test_type,locator,value,keycode from %s" % table
    data = py_mysql.mysql(sql1)
    CommonPublic.log(data)
    return data


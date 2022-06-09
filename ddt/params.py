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
    from models.model_sql import PyMysql
    sql1 = "select * from %s" % table
    data = PyMysql.mysql(sql1)
    CommonPublic.log(data)
    return data



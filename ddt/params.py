import yaml
import os
import xlrd
# def loop_directory():
#     '''循环目录中的文件'''
#     for filename in os.listdir('../lib/cases'):
#         if filename.endswith(".yaml"):
#             file_directory = os.path.join('../lib/cases',filename)
#             file_directory = [file_directory]
#             # file_directory.append('file_directory')
#         else:
#             continue
#
#         file_directory.append(filename)
#         print(file_directory)
#         print(type(file_directory))
#

#
# def yaml_params():
#     import yaml
#     datas = None
#     with open('lib/cases/cases1.yaml',encoding='utf8') as f:
#         datas = yaml.safe_load(f)
#     return datas




# def excel_params():
#     from models.model_excel import sheet_to_list
#     table_sheet = sheet_to_list("lib/cases/A2103.xlsx", 'Sheet1')
#     #print(table)
#     return table_sheet

def excel_params():
    from models.model_excel import sheet_to_list
    table_sheet = sheet_to_list("lib/cases/测试用例.xlsx")
    #print(table_sheet)
    return table_sheet

def app_excel_params():
    from models.model_excel import sheet_to_list
    app_table_sheet = sheet_to_list("lib/appcase/测试用例.xlsx")
    #print(table_sheet)
    return app_table_sheet

def demo_sql_params():
    from models.model_sql import py_mysql
    py_mysql=py_mysql()
    sql1 = 'sql'
    data = py_mysql.mysql(sql1)
    return data


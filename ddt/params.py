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
    sql1 = "select * from %s order by grop" % table
    data = PyMysql.case(sql1)
    return data


def demo_sql_params_group(table):
    """
    用例分组
    :param table: 表名
    :return: sum_case 分组后的用例
    """
    from models.model_sql import PyMysql
    sql0 = "select count(DISTINCT grop) from %s" % table
    sql1 = "select * from %s order by grop" % table
    testcase_group_int = PyMysql.mysql(sql0)
    data = PyMysql.case(sql1)
    # CommonPublic.log("用例为%s，用例共分%s组" % (data, testcase_group_int))

    table = data
    table_case = list()
    sum_case = list()
    if len(table) != '':
        testcase_group_int = testcase_group_int[0][0]
        for i in range(0, testcase_group_int):
            i = 0
            table_case = []
            sum_list = []
            table_case.append(table[i])
            sum_list.append(i)
            for y in range(1, len(table)):
                if table[i][1] == table[y][1]:
                    sum_list.append(y)
                    table_case.append(table[y])
                else:
                    pass
            sum_case.append(table_case)
            for v in range(len(sum_list) - 1, -1, -1):
                del table[sum_list[v]]
            continue
    else:
        pass
    return sum_case


if __name__ == '__main__':
    a = demo_sql_params('app_test')



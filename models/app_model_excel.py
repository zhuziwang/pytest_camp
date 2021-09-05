import xlrd
'''
使用单个excel表中的一个sheet
'''
# def sheet_to_list(excel_file_path,sheet_name):
#     lst = []
#     with xlrd.open_workbook(excel_file_path) as f:
#         table = f.sheet_by_name(sheet_name)
#         for row in range(0,table.nrows):
#             lst.append([])
#             for col in range(0,table.ncols):
#                 #ctype为1是字符串，ctype为2是数值。
#                 cell_type = table.cell(row,col).ctype
#                 cell_value = table.cell_value(row,col)
#                 if cell_type == 1:
#                     lst[row].append(cell_value.strip())
#                 elif cell_type == 2 and cell_value == round(cell_value):
#                     lst[row].append(int(cell_value))
#                 else:
#                     lst[row].append(cell_value)
#     return lst

'''
使用单个excel表表中的多个sheet
'''
def sheet_to_list (excel_file_path):
    lst = []
    row_num = 0
    with xlrd.open_workbook(excel_file_path) as f:
        sheet_all = f.sheet_names()
        for i in range(0,len(sheet_all)):
            table = sheet_all[i]
            table = f.sheet_by_name(table)
            row_int = 0
            for row in range(0, table.nrows):
                lst.append([])
                for col in range(0, table.ncols):
                    cell_type = table.cell(row, col).ctype
                    cell_value = table.cell_value(row, col)
                    if cell_type == 1:
                        lst[row_num].append(cell_value.strip())
                    elif cell_type == 2 and cell_value == round(cell_value):
                        lst[row_num].append(int(cell_value))
                    else:
                        lst[row_num].append(cell_value)
                row_num = row_num + 1
    return lst

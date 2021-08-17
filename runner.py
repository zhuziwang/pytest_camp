
import os
import pytest

#启动yaml的

# from ddt.params import yaml_params
# datas=yaml_params()
#
# print(datas)
# pytest.main(['-s','ddt/login.py','--alluredir','temp','-s'])
# os.system('allure generate temp -o report --clean')


#启动excel的
from ddt.params import excel_params
table_sheet=excel_params()
#print(table_sheet)
pytest.main(['-s','ddt/login_excel.py','--alluredir','temp','-s'])
os.system('allure generate temp -o report/html --clean')
# os.system('copy environment.properties report\environment.properties')
os.system('allure open report/html')
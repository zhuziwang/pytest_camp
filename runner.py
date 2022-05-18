import os
import pytest

#启动web
pytest.main(['-s','ddt/test_demo.py','--alluredir','temp','-s'])
os.system('allure generate temp -o report/html --clean')
#os.system('allure open report/html')

#启动app
# pytest.main(['-s','ddt/app_login_excel.py','--alluredir','temp','-s'])
# os.system('allure generate temp -o report/html --clean')


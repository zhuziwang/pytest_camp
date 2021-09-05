import allure
import pytest
import time
from Web.em import youjian
from Web.appkeys import AppKey
from ddt.params import app_excel_params
app_table_sheet = app_excel_params()
@allure.feature('kouyu100app')
class Test_Commerce:
    num = 1
    title = ''
    def setup_class(self):
        self.web = AppKey()

    def setup_method(self):
        table_ncols = app_table_sheet[Test_Commerce.num:Test_Commerce.num + 1][0]
        Test_Commerce.title = table_ncols[0:][0]
    @allure.story('用例:%s'%title)
    @pytest.mark.parametrize('table', app_table_sheet[1:])
    def test_login(self,table):
        testcases = table[2:]
        testcasess = table[1]
        testcases = [i for i in testcases if i != '']
        func = getattr(self.web, testcases[0])
        values = testcases[1:]
        if testcases[0] == 'assert_results':
            assert_results = func(*values)
            Deserved_results = self.web.Deserved_results
            try:
                assert assert_results == Deserved_results, 'F'
                print('T')
                print(testcasess)

            except AssertionError as e:
                print(e)
                print(testcasess)
                pass
        elif testcases[0] == 'is_displayed':
            is_displayed = func(*values)
            try:
                assert is_displayed == True
                print('T')
                print(testcasess)
            except AssertionError:
                print('F')
                print(testcasess)
                pass
        elif testcases[0] =='title1':
            title = func(*values)
            try:
                assert title == testcases[1]
                print('T')
                print(testcasess)
            except AssertionError:
                print('F')
                print(testcasess)
                pass
        else:
            func(*values)
            print('T')
            print(testcasess)
            time.sleep(0.5)

    def teardown_method(self):
        Test_Commerce.num = Test_Commerce.num +1
        print(Test_Commerce.num)
#
# youjian=youjian()
    #
    # def teardown_class(self):
    #     time.sleep(2)
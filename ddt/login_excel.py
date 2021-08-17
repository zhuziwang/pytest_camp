import allure
import pytest
import time

from Web.webkeys import WebKey
from ddt.params import excel_params
table_sheet=excel_params()

#from models.model_excel_title import title
#table_ncols=title('table', table_sheet[1:])

@allure.feature('项目名字')
class Test_Commerce:
    num = 1
    title = ''
    def setup_class(self):
        self.web = WebKey()
        self.web.openbrwser()

    def setup_method(self):
        table_ncols = table_sheet[Test_Commerce.num:Test_Commerce.num + 1][0]
        Test_Commerce.title = table_ncols[0:][0]
        print(table_ncols)
        print(Test_Commerce.title)
        print(Test_Commerce.num)
        print(Test_Commerce.title)


    @allure.story('用例title的名称:%s'%title)
    @pytest.mark.parametrize('table', table_sheet[1:])
    def test_login(self,table):
        testcases = table[2:]
        testcases = [i for i in testcases if i != '']
        func = getattr(self.web, testcases[0])
        values = testcases[1:]
        allure_step = table[1:2]


        if testcases[0] == 'assert_results':
            with allure.step('测试步骤,%s'%allure_step):
                pass
            assert_results = func(*values)
            Deserved_results = self.web.Deserved_results
            try:
                assert assert_results == Deserved_results, '错误'
            except AssertionError as e:
                assert assert_results == Deserved_results
            else:
                with allure.step('测试步骤,%s' % allure_step):
                    pass
                func(*values)
            finally:
                with allure.step('测试步骤,%s' % allure_step):
                    pass
                    func(*values)
        else:
            print('正确')
            with allure.step('测试步骤,%s'%allure_step):
                pass
            func(*values)


    def teardown_method(self):
        Test_Commerce.num = Test_Commerce.num +1
        print(Test_Commerce.num)

    def teardown_class(self):
        time.sleep(2)
        self.web.quit()
###
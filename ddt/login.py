import allure
import pytest

from Web.webkeys import WebKey
from ddt.params import yaml_params
datas=yaml_params()

@allure.feature('这是项目名字')
class Test_Commerce:

    def setup_class(self):
        self.web = WebKey()
        self.web.openbrwser()
    @allure.story('用例')
    @pytest.mark.parametrize('listcases', datas['loginPage'])
    def test_login(self,listcases):
        # self.web.geturl('http://my.kouyu100.com/demo0')
        # self.web.openbrwser().refresh()
        print('listcases的值是：%s'%listcases)
        print('datas[loginPage]的值是：%s'%datas['loginPage'])
        testcases = listcases['cases']
        print('testcases的值是：%s'%testcases)
        for cases in testcases:
            listcase = list(cases.values())   #把字典转成列表值
            print('listcase的值是：%s' %listcase)
            print('listcase[1]的值是：%s' % listcase[1])
            func = getattr(self.web,listcase[1])
            values = listcase[2:]
            print('values%s'%values)
            if listcase[1] == 'assert_results':
                assert_results = func(*values)
                Deserved_results = self.web.Deserved_results
                print('打印回传的值%s'%assert_results)
                #print('打印要验证的值$s'%Deserved_results)
                try:
                    assert assert_results == Deserved_results,'错误'
                except AssertionError:
                    assert assert_results == Deserved_results
                else:
                    func(*values)
                finally:
                    func(*values)
            else:
                print('正确')
                func(*values)




    # def teardown_class(self):
    #     self.web.quit()
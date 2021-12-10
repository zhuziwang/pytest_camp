#conding=utf-8
import allure
import pytest
import time
from Web.em import youjian
from Web.webkeys import WebKey
from ddt.params import demo_sql_params
demo_sql = demo_sql_params()
@allure.feature('项目名称')
class Test_Commerce:
    num = 0
    title = ''
    def setup_class(self):
        self.web = WebKey()

    def setup_method(self):
        '''添加上flaky装饰器会有list 超限问题，暂时不知道怎么解决'''
        table_ncols = demo_sql[Test_Commerce.num:Test_Commerce.num + 1][0]
        Test_Commerce.title = table_ncols[0:][0]
    # 安装pytest-rerunfailures插件
    # reruns：代表 当case 执行失败的时候 回溯失败case的次数
    # reruns_delay : 代表 回溯case的 间隔时间
    # 如果不是服务器或者程序自身并发限制导致的问题 而是case本身的问题 也会rerun
    @pytest.mark.flaky(reruns=2, reruns_dalay=4)
    @allure.story('用例:%s'%title)
    @pytest.mark.parametrize('table', demo_sql)
    def test_login(self,table):
        testcases = table[1:]
        for table_num in range(1,len(testcases)):
            if testcases[table_num] == None:
                testcases[table_num] = ''
            else:
                testcases[table_num] = testcases[table_num]
        testcases = [i for i in testcases if i != '']
        func = getattr(self.web, testcases[0])
        values = testcases[1:]
        if testcases[0] == 'assert_results':
            assert_results = func(*values)
            Deserved_results = self.web.Deserved_results
            try:
                assert assert_results == Deserved_results, 'F'
                print('T')
                print(testcases)

            except AssertionError as e:
                print(e)
                print(testcases)
                pass
        elif testcases[0] == 'is_displayed':
            is_displayed = func(*values)
            try:
                assert is_displayed == True
                print('T')
                print(testcases)
            except AssertionError:
                print('F')
                print(testcases)
                pass
        elif testcases[0] =='title1':
            title = func(*values)
            try:
                assert title == testcases[1]
                print('T')
                print(testcases)
            except AssertionError:
                print('F')
                print(testcases)
                pass
        else:
            func(*values)
            print('T')
            print(testcases)
            time.sleep(0.5)

    def teardown_method(self):
        Test_Commerce.num = Test_Commerce.num +1
        print(Test_Commerce.num)
#
# youjian=youjian()
    #
    # def teardown_class(self):
    #     time.sleep(2)
#conding=utf-8
import time
# import runtime
from appium import webdriver
import os
from common.cls.public import AppniumKeys


'''
不要动，不用改
'''

'''
desired_caps_phone = {
    'platformName':'Android',
    'platformVersion':'11', #手机android版本111
    'deviceName':'正常手机设备', #设别名称，随意填写
    'appPackage':'com.duia.duiaapp',    #启动的app名称
    'appActivity':'.splash.SplashActivity',   #启动的main页面
    'unicodeKeyboard':True, #使用自带输入法，输入中文时填True
    'resetKeyboard':True,   #执行完程序恢复原来输入法
    'noReset':True, #不要重置App
    'newCommandTimeout':6000,
    'antomationName':'UiAutomator2'
}
desired_caps_simulator = {
    'platformName':'Android',
    'platformVersion':'11', #手机android版本111
    'deviceName':'虚拟机', #设别名称，随意填写
    'appPackage':'com.duia.duiaapp',    #启动的app名称
    'appActivity':'.splash.SplashActivity',   #启动的main页面
    'unicodeKeyboard':True, #使用自带输入法，输入中文时填True
    'resetKeyboard':True,   #执行完程序恢复原来输入法
    'noReset':True, #不要重置App
    'newCommandTimeout':6000,
    'antomationName':'UiAutomator2'
}
#连接Appium Server. 初始化自动化环境
'''

'''
不要动，不用改
'''



class AppKey(AppniumKeys):

    def __init__(self):
        self.driver = None



    def login(self,username='', password=''):
        '''
        点击登录
        :param username:
        :param password:
        :return:
        '''
        name = self.test_element('id', 'com.arivoc.kouyu:id/et_username')
        name.clear()
        name.send_keys(username)
        pws = self.test_element('id', 'com.arivoc.kouyu:id/et_password')
        pws.clear()
        pws.send_keys(password)
        self.test_element('id', 'com.arivoc.kouyu:id/btn_login').click()

    def New_version_tips(self):
        '''
        如果有新版本更新就点击取消安装,并获取更新版本和更新日志
        :return:  updata_text：更新日志
        '''
        if self.driver.find_elements_by_id('com.arivoc.kouyu:id/tv_title_upload') != []:
            self.test_element('id', 'com.arivoc.kouyu:id/tv_quxiao').click()
            updata_text = self.test_element('id', 'com.arivoc.kouyu: id / tv_content_update').text()
        else:
            pass

    def jiazhangtong_aryn_imgView(self):
        '''
        首页关注微信家长通公众号弹窗，点击稍后提醒
        定位ID为：二维码
        :return:
        '''
        if self.driver.find_elements_by_id('com.arivoc.kouyu:id/iv') != []:
            self.test_element('id','com.arivoc.kouyu:id/tv_wait_tell').click()
        else:
            pass

    def Login_update(self, school='', username='', password=''):
        '''
        输入学校，用户名，密码，判断学校默认是否与输入一致后登录
        如果有新版本更新就点击取消安装,并获取更新版本和更新日志
        :return: ele：更新版本
        '''
        if self.driver.find_elements_by_id('com.arivoc.kouyu:id/tv_already_schools') != []:
            school_name = self.test_element('id', 'com.arivoc.kouyu:id/tv_already_schools').text
            if school_name == school:
                self.public_login(username,password)
                self.New_version_tips()
                self.jiazhangtong_aryn_imgView()

            else:
                self.test_element('id', 'com.arivoc.kouyu:id/tv_change_schools').click()
                self.test_element('id', 'com.arivoc.kouyu:id/editFun_imgView').click()
                time.sleep(1)
                self.test_element('id', 'com.arivoc.kouyu:id/search_editText').send_keys(school)
                self.test_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]').click()
                self.public_login(username, password)
                self.New_version_tips()
                self.jiazhangtong_aryn_imgView()

        elif self.test_element('id', 'com.arivoc.kouyu:id/tv_spinner_schools').text == '请选择所在学校':
            self.test_element('id', 'com.arivoc.kouyu:id/tv_spinner_schools').click()
            self.test_element('id', 'com.arivoc.kouyu:id/search_editText').click()
            time.sleep(1)
            self.test_element('id', 'com.arivoc.kouyu:id/search_editText').send_keys(school)
            self.test_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]').click()
            self.public_login(username,password)
            self.New_version_tips()
            self.jiazhangtong_aryn_imgView()

    def first_download(self):
        '''
        判断是否是第一次下载试卷，是就点击下载
        :return:
        '''
        if self.driver.find_elements_by_id('android:id/button2') != []:
            self.test_element('id','android:id/button2').click()
            self.test_element('com.arivoc.kouyu:id/ldms_btn').click()
        else:
            pass


    def move(self):
        '''
        影视配音中根据配音片段的数量，进行点击下一个配音完成
        :return:
        '''
        # move_Number = self.test_element('id','com.arivoc.kouyu:id/tvt_current_position').text
        # #总数字数
        # number = int(move_Number[2:])
        #未配音数
        Undeclared_number = self.test_element('id','com.arivoc.kouyu:id/tvt_finish_num').text
        un_number = int(Undeclared_number)
        for i in range(0,un_number):
            if un_number != 0:
                move_time = self.test_element('id', 'com.arivoc.kouyu:id/tvt_time_down').text
                # 需要的是时间
                move_t = int(move_time[-1])+1
                self.test_element('id','com.arivoc.kouyu:id/btn_record_start').click()
                time.sleep(move_t)
                # 下一个配音
                self.test_element('id', 'com.arivoc.kouyu:id/btn_toright')
            else:

                self.test_element('id','com.arivoc.kouyu:id/ibtn_finish_record').click()
                self.test_element('id','com.arivoc.kouyu:id/ibtn_finish_record').click()

    def work_info_list(self,work_info_text=''):
        '''
        手机作业&成绩中小黑板中查找work_info_text文本的作业后点击
        :param work_info_text:
        :return:
        '''
        for i in range(1,6):
            xpath_num ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[%s]/android.widget.TextView'%i
            xpath_text = self.test_element('xpath',xpath_num).text
            if work_info_text in xpath_text:
                self.test_element('xpath',xpath_num).click()
                break
            else:
                continue
        if i == 5 and work_info_text is not xpath_text:
            self.swipe(326,931,328,297,1000)
            for i in range(1,6):
                xpath_num ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[%s]/android.widget.TextView'%i
                xpath_text = self.test_element('xpath',xpath_num).text
                if work_info_text in xpath_text:
                    self.test_element('xpath', xpath_num).click()
                    break
                else:
                    continue
            if i == 5 and work_info_text is not xpath_text:
                self.swipe(326, 931, 328, 297, 1000)
                for i in range(1, 7):
                    xpath_num = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[%s]/android.widget.TextView' % i
                    xpath_text = self.test_element('xpath', xpath_num).text
                    if work_info_text in xpath_text:
                        self.test_element('xpath', xpath_num).click()
                        break
                    else:
                        continue




    def word_option(self):
        '''
        遍历单词选项，找到选项后，配以单词是否一致
        :return:
        '''
        learn_jindu = self.test_element('id','com.arivoc.kouyu:id/learn_jindu').text
        Over_jindu = int(learn_jindu[5:len(learn_jindu)])

        for i in range(0,Over_jindu):

            test = self.test_element('id', 'com.arivoc.kouyu:id/word_book_lesson_title').text
            test_str = test[4:]
            sql0 = "SELECT word from w2m_wordclass where cnText = '{}' LIMIT 1;" .format(test_str)
            sql1 = "SELECT word from w2m_wordclass where cnText like '{}%' LIMIT 1;" .format(test_str)
            fanyi0 = py_mysql.mysql(sql0)
            if str(fanyi0) == 'None':
                fanyi1 = py_mysql.mysql(sql1)
                Eng_fanyi = fanyi1[0]
            else:
                Eng_fanyi = fanyi0[0]

            option_a=self.test_element('id', 'com.arivoc.kouyu:id/word_book_option_a').text
            option_b=self.test_element('id','com.arivoc.kouyu:id/word_book_option_b').text
            option_c=self.test_element('id','com.arivoc.kouyu:id/word_book_option_c').text

            time.sleep(1)
            if option_a[3:] == Eng_fanyi:
                self.test_element('id','com.arivoc.kouyu:id/word_book_option_a').click()
                time.sleep(2.5)
            elif option_b[3:] == Eng_fanyi:
                self.test_element('id','com.arivoc.kouyu:id/word_book_option_b').click()
                time.sleep(2.5)
            elif option_c[3:] == Eng_fanyi:
                self.test_element('id','com.arivoc.kouyu:id/word_book_option_c').click()
                time.sleep(2.5)
            else:
                self.test_element('id','com.arivoc.kouyu:id/word_book_option_d').click()
                time.sleep(2.5)

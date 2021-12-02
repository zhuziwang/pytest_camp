#conding=utf-8
import time
# import runtime
from appium import webdriver
import os
from models.sql import py_mysql
py_mysql = py_mysql()


'''
不要动，不用改
'''
desired_caps_phone = {
    'platformName':'Android',
    'platformVersion':'11', #手机android版本111
    'deviceName':'正常手机设备', #设别名称，随意填写
    'appPackage':'',    #启动的app名称
    'appActivity':'',   #启动的main页面
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
    'appPackage':'',    #启动的app名称
    'appActivity':'',   #启动的main页面
    'unicodeKeyboard':True, #使用自带输入法，输入中文时填True
    'resetKeyboard':True,   #执行完程序恢复原来输入法
    'noReset':True, #不要重置App
    'newCommandTimeout':6000,
    'antomationName':'UiAutomator2'
}
#连接Appium Server. 初始化自动化环境
'''
不要动，不用改
'''



class AppKey:

    def __init__(self):
        self.driver = None

    def openapp(self):
        all_appPackage = os.popen('adb shell pm list packages').read()
        AndroidVersion = os.popen('adb shell getprop ro.build.version.release').read()
        appPackage = 'com.arivoc.kouyu'
        if appPackage in all_appPackage:
            desired_caps_phone['platformVersion'] = AndroidVersion
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps_phone)
            self.driver.implicitly_wait(20)
        else:
            desired_caps_simulator['platformVersion'] = AndroidVersion
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps_simulator)
            self.driver.implicitly_wait(20)


    def test_element(self, ele_type='', locator='',num=None):
        '''
        accessibility_id对应content-desc
        :param ele_type:    textContains：文本包含
                            textMatches：文本正则
                            textStartsWith：文本起始匹配
        :param locator:
        :return:
        '''
        ele = None
        self.ele = None
        if ele_type == 'accessibility_id':
            ele = self.driver.find_element_by_accessibility_id(locator)
        elif ele_type == 'id':
            ele = self.driver.find_element_by_id(locator)
        elif ele_type == 'xpath':
            ele = self.driver.find_element_by_xpath(locator)
        elif ele_type == 'class_name':
            ele = self.driver.find_elements_by_class_name(locator)
        elif ele_type == 'name':
            ele = self.driver.find_elements_by_name(locator)
        elif ele_type == 'text':
            ele = self.driver.find_element_by_new_UiSelector().text(locator)
        elif ele_type == 'textContains':
            ele = self.driver.find_element_by_new_UiSelector().textContains(locator)
        elif ele_type == 'textMatches':
            ele = self.driver.find_element_by_new_UiSelector().textMatches(locator)
        elif ele_type == 'textStartsWith':
            ele = self.driver.find_element_by_new_UiSelector().textStartsWith(locator)
        elif ele_type == 'android_uiautomator_text':
            ele = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%locator)
            print (ele.text)
        elif ele_type == 'xpaths':
            ele = self.driver.find_elements_by_xpath(locator)
        self.ele = ele
        return ele

    def public_login(self,username=None,password=None):
        ele = self.test_element('id', 'com.arivoc.kouyu:id/et_username')
        ele.clear()
        ele.send_keys(username)
        ele1 = self.test_element('id', 'com.arivoc.kouyu:id/et_password')
        ele1.clear()
        ele1.send_keys(password)
        self.test_element('id','com.arivoc.kouyu:id/btn_login').click()
        #选择用户登录，提示文字的xpath
        xpath_xpath='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]'
        if self.test_element('xpaths',xpath_xpath) != []:
            rename_list = self.test_element('xpaths', xpath_xpath).text
            rname_text = ''.join(rename_list)
            if rname_text == '你登录的账号存在多个重名账号，请选择你自己的账号。':
                # xpath_element='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[%d]/android.widget.ImageView[2]'%匹配第几个
                # self.test_element('xpath','xpath_element').click()
                self.test_element('android_uiautomator_text',username).click()
            else:
                pass
        else:
            pass


    def clear(self,ele_type='',locator=''):
        '''
        清空内容
        :param ele_type:
        :param locator:
        :return:
        '''
        ele = self.test_element(ele_type, locator)
        ele.clear()

    def click(self,ele_type='',locator='',num=None):
        '''
        点击
        '''
        if num == None:
            self.test_element(ele_type,locator).click()
        else:
            ele = self.test_element(ele_type,locator,num)
            ele[num].click()

    def send_keys(self,ele_type='',locator='',send='',num=None):
        '''
        输入内容
        '''
        if num == None:
            self.test_element(ele_type, locator).send_keys(send)
        else:
            ele = self.test_element(ele_type,locator,num)
            ele[num].send_keys(send)

    def driver_time(self,dtime=None):
        time.sleep(float(dtime))

    def backgroud_app(self,time=None):
        '''
        :backgroud_app: 把应用置于后台time时间后唤醒到前台
        :return:
        '''
        self.driver.backgroud_app(time)

    def lock(self,time=None):
        '''
        :lock: 手机进入锁屏状态time时间后，再次唤醒
        :return:
        '''
        self.driver.lock(time)

    def hide_keyboard(self):
        '''
        :hide_keyboard: 隐藏键盘
        '''
        self.driver.hide_keyboard()

    def start_activity(self,apappPackagep='',appActivity=''):
        '''
        启动一个app或者在当前app中打开一个新的activity，仅适用于android
        :param apappPackagep: 启动的app名称
        :param appActivity: 启动的main页面
        :return:
        '''
        self.driver.start_activity(apappPackagep,appActivity)

    def is_app_installed(self,apappPackagep=''):
        '''
        检查app是否被安装
        :param apappPackagep: app名称
        :return:
        '''
        app_installed = self.driver.is_app_installed(apappPackagep)
        return app_installed

    def install_app(self,appPackagep=''):
        '''
        安装app
        :param appPackagep: app名称 例如：xx.apk
        :return:
        '''
        self.driver.install_app(appPackagep)

    def remove_app(self,apappPackagep=''):
        '''
        卸载app
        :param apappPackagep: app名称
        :return:
        '''
        self.driver.remove_app(apappPackagep)

    def close_app(self):
        '''
        关闭app
        :return:
        '''
        self.driver.close_app()

    def launch_app(self):
        '''
        如果测试中的应用程序（AUT）已关闭，或处于后台，它将启动它。如果AUT已经打开，它将对其进行背景设置并重新启动。
        :return:
        '''
        self.driver.launch_app()

    def press_keycode(self,num=None):
        '''
        输入键值
        :param num: 3、HOME键
                    82、菜单键
                    4、返回键
                    26、电源键
                    66、回车键
                    64、退格键
        :return:
        '''
        if num == 3:
            self.driver.press_keycode(3)
        elif num == 82:
            self.driver.press_keycode(82)
        elif num == 4:
            self.driver.press_keycode(4)
        elif num ==26:
            self.driver.press_keycode(26)
        elif num ==26:
            self.driver.press_keycode(66)
        elif num ==67:
            self.driver.press_keycode(67)

    def get_window_size(self):
        '''
        获取当前窗口大小
        :return:
        '''
        get_windows_size = self.driver.get_window_size()
        return get_windows_size

    def swipe(self,start_x=None,start_y=None,end_x=None,end_y=None,duration=None):
        '''
        滑动屏幕
        :param duration: 移动的时间间隔
        :return:
        '''
        self.driver.swipe(start_x,start_y,end_x,end_y,duration)

    def get_screenshot_as_file(self,file_path=''):
        '''
        截图，并保存
        :param file_path: 路径
        :return:
        '''
        self.driver.get_screenshot_as_file(file_path)

    def text(self, ele_type='', locator=''):
        '''
        获取元素的text属性值
        :param ele_type:
        :param locator:
        :return:
        '''
        text = self.driver.test_element(ele_type,locator).text
        return text

    def content_desc(self, ele_type='', locator=''):
        '''
        获取元素content_desc属性值
        :param ele_type:
        :param locator:
        :return:
        '''
        content_desc = self.driver.test_element(ele_type,locator)
        return content_desc

    def currentActivity(self):
        '''
        获取当前界面的activity
        :return:
        '''
        currentActivity = self.driver.currentActivity()
        return currentActivity

    def openNotifications(self):
        '''
        打开通知栏界面
        :return:
        '''
        self.driver.openNotifications()

    def getNetworkConnection(self):
        int_status = self.driver.getNetworkConnection().value
        return int_status

    # def Runtime_getruntime_exec(self,adb=''):
    #     '''
    #     启动系统命令
    #     :param adb:
    #     :return:
    #     '''
    #     runtime.getruntime().exec(adb)

    def assert_results(self,ele_type=None,locator=None,Deserved_results=None):
        '''text断言'''
        self.Deserved_results = Deserved_results
        Actual_results = self.test_element(ele_type,locator).text
        return Actual_results


    def qzdj(self,ele_type=None,locator=None):
        '''
        强制点击（元素被遮挡后使用）
        :param ele_type:
        :param locator:
        :return:
        '''
        qzdj = self.test_element(ele_type,locator)
        self.driver.execute_script('arguments[0].click()',qzdj)
        return qzdj

    def current_url(self):
        '''
        获得当前页面的URL
        Returns
        -------
        '''
        now_url = self.driver.current_url
        return now_url

    def title(self,test=None):
        '''
       获得当前页面的标题
        Returns
        -------
        '''
        title = self.driver.title
        print(title)
        return title

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

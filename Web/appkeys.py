import time
# import runtime
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions .android.nativekey import AndroidKey


desired_caps = {
    'platformName':'Android',
    'platformVersion':'11', #手机android版本
    'deviceName':'localhost', #设别名称，随意填写
    'appPackage':'com.arivoc.kouyu',    #启动的app名称
    'appActivity':'com.arivoc.kouyu100.WelcomeActivity',   #启动的main页面
    'unicodeKeyboard':True, #使用自带输入法，输入中文时填True
    'resetKeyboard':True,   #执行完程序恢复原来输入法
    'noReset':True, #不要重置App
    'newCommandTimeout':6000,
    'antomationName':'UiAutomator2'
}
#连接Appium Server. 初始化自动化环境




class AppKey:

    def __init__(self):
        self.driver = None

    def openapp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(20)

    def test_element(self, ele_type='', locator=''):
        '''
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
        elif ele_type == 'name':
            ele = self.driver.find_element_by_name(locator)
        elif ele_type == 'text':
            ele = self.driver.find_element_by_new_UiSelector().text(locator)
        elif ele_type == 'textContains':
            ele = self.driver.find_element_by_new_UiSelector().textContains(locator)
        elif ele_type == 'textMatches':
            ele = self.driver.find_element_by_new_UiSelector().textMatches(locator)
        elif ele_type == 'textStartsWith':
            ele = self.driver.find_element_by_new_UiSelector().textStartsWith(locator)
        elif ele_type == 'android_uiautomator_text':
            ele = self.driver.find_element_by_android_uiautomator('new UiSelector().text(%s)')%locator
            print (ele.text)
        self.ele = ele
        return ele

    def clear(self,ele_type='',locator=''):
        '''
        清空内容
        :param ele_type:
        :param locator:
        :return:
        '''
        ele = self.test_element(ele_type, locator)
        ele.clear()

    def click(self,ele_type='',locator=''):
        '''
        点击
        '''
        self.test_element(ele_type,locator).click()

    def send_keys(self,ele_type='',locator='',send=''):
        '''
        输入内容
        '''
        self.test_element(ele_type, locator).send_keys(send)

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

    def New_version_tips(self):
        '''
        如果有新版本更新就点击取消安装
        :return:
        '''
        ele = self.test_element('id','com.arivoc.kouyu:id/tv_title_upload').text
        version_a = '发现新版本'
        if version_a in ele:
            self.test_element('id','com.arivoc.kouyu:id/tv_quxiao').click()
            # updata_text = self.test_element('id','com.arivoc.kouyu: id / tv_content_update').text()
        else:
            pass

    def Login_update(self,school='',username='',password=''):
        '''
        输入学校，用户名，密码，判断学校默认是否与输入一致后登录
        如果有新版本更新就点击取消安装,并获取更新版本和更新日志
        :return: ele：更新版本
        '''

        if self.test_element('id','com.arivoc.kouyu:id/tv_already_schools').get_attribute('textContent') == school :
            name = self.test_element('id','com.arivoc.kouyu:id/et_username')
            name.clear()
            name.send_keys(username)
            pws = self.test_element('id','com.arivoc.kouyu:id/et_password')
            pws.clear()
            pws.send_keys(password)
            self.test_element('id','com.arivoc.kouyu:id/btn_login').click()
            ele = self.test_element('id','com.arivoc.kouyu:id/tv_title_upload').get_attribute('textContent')
            version_a = '发现新版本'
            if version_a in ele:
                self.test_element('id','com.arivoc.kouyu:id/tv_quxiao').click()
                updata_text = self.test_element('id','com.arivoc.kouyu: id / tv_content_update').text()
                return ele,updata_text
            else:
                pass
        elif self.test_element('id','com.arivoc.kouyu:id/tv_already_schools').get_attribute('textContent') is not school:
            self.test_element('id','com.arivoc.kouyu:id/tv_change_schools').click()
            self.test_element('id','com.arivoc.kouyu:id/editFun_imgView').click()
            self.test_element('id','com.arivoc.kouyu:id/editFun_imgView').send_keys(school)
            self.test_element('xpath','	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]').click()

            name = self.test_element('id', 'com.arivoc.kouyu:id/et_username')
            name.clear()
            name.send_keys(username)
            pws = self.test_element('id', 'com.arivoc.kouyu:id/et_password')
            pws.clear()
            pws.send_keys(password)
            self.test_element('id', 'com.arivoc.kouyu:id/btn_login').click()
            ele = self.test_element('id', 'com.arivoc.kouyu:id/tv_title_upload').get_attribute('textContent')
            version_a = '发现新版本'
            if version_a in ele:
                self.test_element('id', 'com.arivoc.kouyu:id/tv_quxiao').click()
                updata_text = self.test_element('id', 'com.arivoc.kouyu: id / tv_content_update').text()
                return ele, updata_text
            else:
                pass
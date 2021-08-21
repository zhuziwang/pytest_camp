from appium import webdriver
from appium.webdriver.extensions .android.nativekey import AndroidKey

desired_caps = {
    'platformName':'Android',
    'platformVersion':'6.0.1', #手机android版本
    'deviceName':'localhost', #设别名称，随意填写
    'appPackage':'com.tencent.mobileqq',    #启动的main页面
    'appActivity':'.activity.SplashActivity',
    'unicodeKeyboard':True, #使用自带输入法，输入中文时填True
    'resetKeyboard':True,   #执行完程序恢复原来输入法
    'noReset':True, #不要重置App
    'newCommandTimeout':6000,
    'antomationName':'UiAutomator2'
}

#连接Appium Server. 初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.implicitly_wait(20)

el2 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
el2.clear()
el2.send_keys("2192094143")
el3 = driver.find_element_by_accessibility_id("密码 安全")
el3.clear()
el3.send_keys("zhuzw112233.")
el1 = driver.find_element_by_accessibility_id("登 录")
el1.click()
el2 = driver.find_element_by_accessibility_id("帐户及设置")
el2.click()
el3 = driver.find_element_by_accessibility_id("设置")
el3.click()
el4 = driver.find_element_by_accessibility_id("帐号管理")
el4.click()
el5 = driver.find_element_by_accessibility_id("退出")
el5.click()
el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.Button")
el6.click()
el7 = driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")
el7.click()

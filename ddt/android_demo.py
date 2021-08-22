import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions .android.nativekey import AndroidKey


desired_caps = {
    'platformName':'Android',
    'platformVersion':'6.0.1', #手机android版本
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
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.implicitly_wait(20)

#登录qq
# el2 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
# el2.clear()
# el2.send_keys("2192094143")
# el3 = driver.find_element_by_accessibility_id("密码 安全")
# el3.clear()
# el3.send_keys("zhuzw112233.")
# el1 = driver.find_element_by_accessibility_id("登 录")
# el1.click()
# el2 = driver.find_element_by_accessibility_id("帐户及设置")
# el2.click()
# el3 = driver.find_element_by_accessibility_id("设置")
# el3.click()
# el4 = driver.find_element_by_accessibility_id("帐号管理")
# el4.click()
# el5 = driver.find_element_by_accessibility_id("退出")
# el5.click()
# el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.Button")
# el6.click()
# el7 = driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")
# el7.click()


#登录kouyu100

if driver.find_element_by_id('com.arivoc.kouyu:id/tv_already_schools').text == '请选择所在学校':
    driver.find_element_by_id('com.arivoc.kouyu:id/tv_already_schools').click()
    time.sleep(1)
    area_rdoBtn_province = driver.find_element_by_android_uiautomator('new UiSelector().text("北京")').click()
    # area_rdoBtn_province = driver.find_elements_by_id('com.arivoc.kouyu:id/area_rdoBtn')[0].click()
    time.sleep(1)
    area_rdoBtn_city = driver.find_elements_by_id('com.arivoc.kouyu:id/area_rdoBtn')[1].click()

    time.sleep(1)
    area_rdoBtn_area = driver.find_elements_by_id('com.arivoc.kouyu:id/area_rdoBtn')[1].click()
    time.sleep(1)
    driver.swipe(start_x=600, start_y=1600, end_x=600, end_y=300, duration=800)
    time.sleep(1)
    area_rdoBtn_school = driver.find_elements_by_id('com.arivoc.kouyu:id/name_tView')[2].click()
else:
    spinner_schools = driver.find_element_by_id('com.arivoc.kouyu:id/tv_change_schools')
    spinner_schools.click()
    time.sleep(1)
    choice_province = driver.find_element_by_android_uiautomator('new UiSelector().text("北京")').click()
    time.sleep(1)
    area_rdoBtn_province = driver.find_elements_by_id('com.arivoc.kouyu:id/content')[0].click()
    time.sleep(1)
    area_rdoBtn_city = driver.find_elements_by_id('com.arivoc.kouyu:id/area_rdoBtn')[1].click()

    time.sleep(1)
    area_rdoBtn_area = driver.find_elements_by_id('com.arivoc.kouyu:id/area_rdoBtn')[1].click()
    time.sleep(1)
    driver.swipe(start_x=600, start_y=1600, end_x=600, end_y=300, duration=800)
    time.sleep(1)
    area_rdoBtn_school = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[7]').click()

driver.find_element_by_id('com.arivoc.kouyu:id/et_username').send_keys('a30')
driver.find_element_by_id('com.arivoc.kouyu:id/et_password').send_keys('ky100yanshi')
driver.find_element_by_id('com.arivoc.kouyu:id/btn_login').click()

loc='//*[contains(@text,"{}")]'.format("无该用户")
try:
    driver.find_element_by_xpath(loc)
    # 上限10秒就够了，确认toast在页面上存在的时候大概是多久，它都没有0.5秒，你去间隔0.5，可能消失了，你还只留在这。
    print(driver.find_element_by_xpath(loc).text)
except:
    print("没有找到匹配的toast！！！！")


if driver.find_element_by_id('com.arivoc.kouyu:id/tv_content_update').text == '1. 修复已知BUG，提高稳定性':
    print('需要升级')
else:
    print('不需要升级')
#不升级，点击取消按钮
area_rdoBtn_province = driver.find_element_by_android_uiautomator('new UiSelector().text("取消")').click()
time.sleep(2)
driver.find_element_by_id('com.arivoc.kouyu:id/iv_home_ai').click()

time.sleep(5)
driver.find_element_by_accessibility_id("AI对话训练 ").click()

driver.find_element_by_id("com.arivoc.kouyu:id/back_imgView").click()

driver.find_element_by_accessibility_id("和Aryn智能对话 去对话").click()

driver.find_element_by_accessibility_id("ok").click()

driver.find_element_by_accessibility_id("pattern_gray")

el10 = driver.find_element_by_accessibility_id("开始和Aryn聊天吧~")
el10.send_keys("hello")
driver.find_element_by_accessibility_id("send").click()

driver.find_element_by_id("com.arivoc.kouyu:id/close_imgView").click()

driver.find_element_by_id("com.arivoc.kouyu:id/tv_read_confirm").click()


time.sleep(5)








driver.quit()
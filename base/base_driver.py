from appium import webdriver

def init_driver():
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.108.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.android.mms'
    desired_caps['appActivity'] = '.ui.ConversationList'

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
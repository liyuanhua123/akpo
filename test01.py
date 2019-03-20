import pytest
from appium import webdriver
import time
class TestAKLogin():

    def setup(self):
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app信息
        desired_caps['appPackage'] = 'com.vcooline.aike'
        desired_caps['appActivity'] = '.umanager.LoginActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown(self):
        time.sleep(5)

        self.driver.quit()
#com.vcooline.aike:id/etxt_username    com.vcooline.aike:id/etxt_pwd  com.vcooline.aike:id/btn_login
    def test_erro_username(self):
         self.driver.find_element_by_id("com.vcooline.aike:id/etxt_username").send_keys("122342")
         self.driver.find_element_by_id("com.vcooline.aike:id/etxt_pwd").send_keys("1234455")
         self.driver.find_element_by_id("com.vcooline.aike:id/btn_login").click()
    def test_username_none(self):

        pass
    def test_login(self):
        pass

if __name__ == '__main__':

    pytest.main("-s test01.py")



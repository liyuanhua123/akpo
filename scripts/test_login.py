"""
    类名：大驼峰将模块名搬进来，去掉下划线
    方法：
        setup
        teardown
        测试方法
"""
import os
import sys
sys.path.append(os.getcwd())

from base.get_driver import get_driver


# 新建 登录测试类
from page.page_login import PageLogin


class TestLogin:

    # setup
    def setup(self):
        # 获取driver
        self.driver = get_driver()
        # 获取页面对象 PageLogin
        self.login = PageLogin(self.driver)

    # teardown
    def teardown(self):
        # 关闭页面对象
        self.driver.quit()

    # 测试方法
    def test_login(self, username="1111", pwd="123456"):
        # 调用 页面对象中 登录业务方法
        self.login.page_login(username, pwd)
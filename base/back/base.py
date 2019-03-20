from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法 封装  给谁用？？？ 点击、输入
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击元素 封装
    def base_click(self, loc):
        # 获取元素并点击
        self.base_find_element(loc).click()

    # 输入元素 封装
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)
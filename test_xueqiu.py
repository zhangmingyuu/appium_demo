from time import sleep, time
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["automationName"] = "uiautomator2"
        caps["deviceName"] = "emulator-5556"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps["dontStopAppOnReset"] = True
        caps["skipServerInstallation"] = True
        caps[
            "chromedriverExecutable"] = "/Users/linlin/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_search(self):
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # el1.click()
        # el2 = self.driver.find_element_by_id("com.xueqiu.android:id/title_img")
        # el2.click()
        self.driver.find_element(MobileBy.ID, "title_img").click()

    # TouchAction 滑动
    def test_swipe(self):
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.implicitly_wait(3)
        width = self.driver.get_window_size()['width']
        print(width)
        height = self.driver.get_window_size()['height']
        TouchAction(self.driver).long_press(x=width * 0.5, y=height * 0.8) \
            .move_to(x=width * 0.5, y=height * 0.2) \
            .release() \
            .perform()

    def test_search_alibaba(self):
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "home_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='股票' and contains(@resource-id,'title_text')]").click()
        price = float(self.driver.find_element(MobileBy.XPATH,
                                               "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]").text)
        assert price > 200
        # get_attribute获取元素属性
        print(self.driver.find_element(MobileBy.XPATH,
                                       "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]").get_attribute(
            "resourceId"))

    # uiselector 查找,--滑动查找某个元素
    def test_uiselector(self):
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        scroll_element = (
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                                          '.scrollIntoView(new UiSelector().text("5小时前").instance(0));')
        self.driver.find_element(*scroll_element).click()

    def get_attribute(self, element, attribute):
        return self.driver.find_element(*element).get_attribute(attribute)

    # 如何保证测试数据是稳定不变的，是预期的测试数据？
    def test_hasadd(self):
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "home_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='股票' and contains(@resource-id,'title_text')]").click()
        add_element_before = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id,'follow_btn')]")
        self.driver.find_element(*add_element_before).click()
        self.driver.implicitly_wait(2)
        # 弹框处理
        if self.driver.find_element(MobileBy.XPATH, "//*[@text='下次再说']").is_displayed():
            self.driver.find_element(MobileBy.XPATH, "//*[@text='下次再说']").click()
            self.driver.find_element(MobileBy.ID, "action_close").click()
            # 再次搜索
            self.driver.find_element(MobileBy.ID, "home_search").click()
            self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
            self.driver.find_element(MobileBy.ID, "name").click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='股票' and contains(@resource-id,'title_text')]").click()
            add_element_after = (
                MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id,'followed_btn')]")
            add_status = self.get_attribute(add_element_after, 'text')
        else:
            self.driver.find_element(MobileBy.ID, "action_close").click()
            # 再次搜索
            self.driver.find_element(MobileBy.ID, "home_search").click()
            self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
            self.driver.find_element(MobileBy.ID, "name").click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='股票' and contains(@resource-id,'title_text')]").click()
            add_element_after = (
                MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id,'followed_btn')]")
            add_status = self.get_attribute(add_element_after, 'text')

        assert add_status == '已添加'

    def test_webview_debug(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易' and contains(@resource-id,'tab_name')]").click()
        # for i in range(5):
        #     print(self.driver.contexts)
        print(self.driver.contexts)
        # WebDriverWait(self.driver,30).until(lambda x:len(self.driver.contexts)>1)
        webview = self.driver.contexts[-1]
        print(webview)
        self.driver.switch_to.context(webview)
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_info_205").click()
        for i in range(5):
            print(self.driver.window_handles)
            sleep(0.5)
        WebDriverWait(self.driver, 10).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone = (By.ID, "phone-number")
        # WebDriverWait(self.driver, 60).until(expected_conditions.invisibility_of_element_located(phone)))
        self.driver.find_element(*phone).send_keys("17316342037")

    def test_meigukaihu(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易' and contains(@resource-id,'tab_name')]").click()
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(By.CSS_SELECTOR,".trade_home_xueying_VAL").click()
        for i in range(5):
            print(self.driver.window_handles)
            sleep(5)
        WebDriverWait(self.driver,10).until(lambda x:len(self.driver.window_handles)>3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone = (By.CSS_SELECTOR,'[placeholder="请输入手机号"]')
        WebDriverWait(self.driver,30).until(expected_conditions.element_to_be_clickable(phone))
        self.driver.find_element(*phone).send_keys("17316342037")
        self.driver.find_element(By.CSS_SELECTOR,'[placeholder="请输入验证码"]').send_keys("1234")
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(MobileBy.ID,"action_bar_close").click()



    def teardown(self):
        pass
        # sleep(20)
        # self.driver.quit()

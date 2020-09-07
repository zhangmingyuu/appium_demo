from time import sleep, time
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["automationName"] = "uiautomator2"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        # caps["noReset"] = False
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        # caps["dontStopAppOnReset"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)


    def test_demoapi(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Views']").click()
        scroll_element = (
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                                          '.scrollIntoView(new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_element).click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Add']").click()
        toast = self.driver.find_element(MobileBy.XPATH, "//*[@class = 'android.widget.Toast']").text
        print(toast)
        assert "Clicked popup menu item Add" == toast
    def teardown(self):
        pass
        # sleep(20)
        # self.driver.quit()
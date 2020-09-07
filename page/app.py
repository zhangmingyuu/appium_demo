from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["automationName"] = "uiautomator2"
            caps["deviceName"] = "emulator-5556"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            caps["unicodeKeyboard"] = True
            caps["resetKeyboard"] = True
            caps["dontStopAppOnReset"] = True
            caps["skipServerInstallation"] = True
            caps[
                "chromedriverExecutable"] = "/Users/linlin/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver"

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(10)

        else:
            self._driver.start_activity()
            self._package, self._activity
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        # todo: wait
        return Main(self._driver)

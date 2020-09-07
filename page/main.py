from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.search import Search


class Main(BasePage):

    def goto_search_page(self):
        self._driver.find_element(MobileBy.ID, "home_search").click()
        return Search(self._driver)

    def goto_hangqing(self):
        pass

    def goto_jijin(self):
        pass

    def goto_jiaoyi(self):
        pass

    def goto_profile(self):
        pass

    def goto_message(self):
        pass
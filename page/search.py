from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class Search(BasePage):

    def search(self, key: str):
        # todo: 输入操作，返回一个搜索结果页
        self._driver.find_element(MobileBy.ID, "search_input_text").send_keys(key)
        self._driver.find_element(MobileBy.ID, "name").click()
        self._driver.find_element(MobileBy.XPATH, "//*[@text='股票' and contains(@resource-id,'title_text')]").click()
        return self

    def get_price(self, key: str) -> float:
        price = float(self._driver.find_element(MobileBy.XPATH,
                                               "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]").text)
        return price

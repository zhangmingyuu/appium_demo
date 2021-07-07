# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

from selenium.webdriver.support.wait import WebDriverWait
import logging

key_code = {
    '0': 7, '1': 8, '2': '9', '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16,
    "@": 77, '.': 56,
    'A': 29, 'B': 30, 'C': 31, 'D': 32, 'E': 33, 'F': 34, 'G': 35, 'H': 36, 'I': 37, 'J': 38,
    'K': 39, 'L': 40, 'M': 41, 'N': 42, 'O': 43, 'P': 44, 'Q': 45, 'R': 46, 'S': 47, 'T': 48,
    'U': 49, 'V': 50, 'X': 52, 'Y': 53, 'Z': 54,
    'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38,
    'k': 39, 'l': 40, 'm': 41, 'n': 42, 'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48,
    'u': 49, 'v': 50, 'w': 51, 'x': 52, 'y': 53, 'z': 54,
    'W': [51, 64, 59]
}


class FindElem:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.poll_frequency = 0.5

    # 根据代码结构，自定义了一个 find_element 和 find_elements 的方法

    def find_element(self, locator):
        logging.info("输出定位信息：{}".format(locator))
        """
        :param locator: 传入定位器参数locator = (By.XX, "value")
        :locator: 返回元素对象
        """

        if not isinstance(locator, tuple):
            logging.error("locator参数类型错误，必须传元组类型：locator = (By.XX, 'value')")
        else:
            logging.info("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))
            # 传入的locator正确，我们就可以使用该locator的信息定位元素了，然后将该定位到的元素return
            try:
                elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    lambda x: x.find_element(*locator)
                )
                logging.info("元素对象为：{}".format(elem))
                return elem
            except Exception as e:
                logging.error("定位不到元素，错误信息为{}".format(e))

    def find_elements(self, locator):
        try:
            elems = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                lambda x: x.find_elements(*locator)
            )
            logging.info("元素对象为：{}".format(elems))
        except Exception as e:
            logging.error("元组对象获取失败，错误信息为：{}".format(e))
        return elems

    def key_event(key: str):
        account = []
        for i in key:
            for j in key_code.keys():
                if i == j:
                    account.append(key_code[j])
        return account

    # 接下来还要重新定义 send_keys, click 等操作方式

    def click(self, locator):
        elem = self.find_element(locator)
        try:
            elem.click()
            logging.info("点击元素成功")
        except Exception as e:
            logging.error("操作失败，错误信息为：{}".format(e))

    def check_existence(self, locator):
        try:
            elem = self.find_element(locator)
            return True
        except Exception as e:
            return False
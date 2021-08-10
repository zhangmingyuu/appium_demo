# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''
import logging
from selenium.webdriver.support.wait import WebDriverWait
from page_object.analyse_element_info import ActivityElem


class FindElem:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.poll_frequency = 0.5
        self.elem_locator = ActivityElem()

    # 根据代码结构，自定义了一个 find_element 和 find_elements 的方法

    def find_element(self, locator):
        """
        :param locator: 要定位的元素的信息，是一个元组类型，定位器参数locator = (By.XX, "value")
        :return: 返回元素对象
        """
        # 先通过传入的参数，找到元素的相关信息，并返回一个元组
        elem_info = self.elem_locator.get_locator(locator)
        logging.info("输出定位信息：{}".format(elem_info))
        # 先判断是不是元组数据
        if not isinstance(elem_info, tuple):
            logging.error("locator参数类型错误，必须传元组类型：locator = (By.XX, 'value')")
        else:
            logging.info("正在定位元素信息：定位方式->%s, value值->%s" % (elem_info[0], elem_info[1]))
            # 传入的locator正确，我们就可以使用该locator的信息定位元素了，然后将该定位到的元素return
            try:
                elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    lambda x: x.find_element(*elem_info)
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

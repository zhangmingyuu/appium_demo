# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import logging
from Pub_method.findElem import FindElem
from Pub_method.read_yaml import ActivityElem


# 继承FindElem，并且重写了FindElem
class ElemActivity(FindElem):
    def __init__(self, driver):
        self.driver = driver
        # __init__中直接调用ActivityElem方法，生成一个ActivityElem的对象
        self.elem_locator = ActivityElem()
        super().__init__(driver)

    # 重新封装了click方法
    def click_btn(self, value):
        # 先获取元素的信息
        elem = self.elem_locator.get_locator(value)
        # 再调用父类的点击元素的方法
        super().click(elem)

    # 普通的send_keys方法
    def send_keys(self, locator, value):
        elem = self.find_element(locator)
        try:
            elem.senk_keys(value)
        except Exception as e:
            logging.error("send_keys失败，错误信息为{}".format(e))


    # 元素是否可以获取到的验证方法
    def elem_enable(self, value):
        # 获取到这个元素
        elem = self.find_element(value)

        # 验证这个元素是否存在
        try:
            result = elem.is_displayed()
            return result
        except BaseException as e:
            return False
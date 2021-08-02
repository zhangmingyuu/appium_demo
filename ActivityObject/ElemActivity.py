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

    # 重新封装查找元素的方法
    # def find_element(self, value):
    #     try:
    #         # 获取元素的信息
    #         elem = self.elem_locator.get_locator(value)
    #         return elem
    #     except Exception as e:
    #         logging.error("没有定位到元素")
    #         return False

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

    def send_key(self, value):
        key = super().key_event(value)
        for i in key:
            if type(i) is int:
                self.driver.press_keycode(i)
            else:
                self.driver.press_keycode(i[0], metastate=i[1], flags=i[2])

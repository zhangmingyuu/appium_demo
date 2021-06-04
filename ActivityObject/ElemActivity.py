# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import logging
from Pub_method.findElem import FindElem
from Pub_method.read_yaml import ActivityElem


class ElemActivity(FindElem):
    def __init__(self, driver):
        self.driver = driver
        self.elem_locator = ActivityElem()
        super().__init__(driver)

    def click_btn(self, value):
        elem = self.elem_locator.get_locator(value)
        super().click(elem)

    def send_keys(self, locator, value):
        elem = self.find_element(locator)
        try:
            elem.senk_keys(value)
        except Exception as e:
            logging.error("send_keys失败，错误信息为{}".format(e))

    def check_exist(self, value):
        elem = self.elem_locator.get_locator(value)
        super().check_existence(elem)

    def send_key(self, value):
        key = super().key_event(value)
        for i in key:
            if type(i) is int:
                self.driver.press_keycode(i)
            else:
                self.driver.press_keycode(i[0], metastate=i[1], flags=i[2])

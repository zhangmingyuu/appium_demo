# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import logging
from page_object.find_element import FindElem
from pub_method.pub_method import PubMethod


# 继承FindElem，并且重写了FindElem
class ElemActivity(FindElem):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_btn(self, locator):
        # 找到这个元素
        elem = super().find_element(locator)
        try:
            elem.click()
            logging.info("点击元素成功")
        except BaseException as e:
            logging.error("操作失败，错误信息为：{}".format(e))

    # 普通的send_keys方法
    def send_keys(self, locator, value):
        elem = super().find_element(locator)
        try:
            elem.senk_keys(value)
        except Exception as e:
            logging.error("send_keys失败，错误信息为{}".format(e))

    # 元素是否可以获取到的验证方法
    def elem_enable(self, locator):
        # 获取到这个元素
        elem = super().find_element(locator)
        # 验证这个元素是否存在
        try:
            result = elem.is_displayed()
            return result
        except BaseException as e:
            return False

    # 获取元素的text
    def elem_text(self, locator):
        # 先去解析，然后再找元素
        # e_value = self.elem_locator.get_locator(value)
        elem = self.find_element(locator)
        # 获取这个元素的text，然后返回
        try:
            text = elem.text
            return text
        except BaseException as e:
            logging.error(e)

    # 安卓特有的向输入框发送内容的方法，当send_keys不好用使，可以使用这个方法
    # 使用方法为，先使用click_btn点击一个下输入框，然后再调用这个方法
    def android_send_keys(self, keys):
        inputs = PubMethod.key_event(keys)
        for i in inputs:
            if isinstance(i, int):
                self.driver.press_keycode(keycode=i)
            else:
                self.driver.press_keycode(keycode=i[0], metastate=i[1], flags=i[2])

    # 滑动屏幕的方法
    def swipe_screen(self, pre_width, pre_height, end_width, end_height):
        """
                :param pre_width: 滑动起点横坐标
                :param pre_height: 滑动起点纵坐标
                :param end_width: 滑动终点横坐标
                :param end_height: 滑动终点纵坐标
                :return: 无返回值
                """
        # 基本的分辨率，用来计算相对坐标系数的，这个值采取的是市场主流屏幕的分辨率
        basic_width = 1080
        basic_height = 2134

        # 获取当前手机的分辨率
        size = self.driver.get_window_size()
        current_width = size['width']
        current_height = size['height']

        # 计算系数，这里还有待完善，按说横坐标和纵坐标的系数只计算一次就可以，这里计算了两次
        width = round(pre_width / basic_width, 2)
        height = round(pre_height / basic_height, 2)
        end_wi = round(end_width / basic_width, 2)
        end_hei = round(end_height / basic_height, 2)
        self.driver.swipe(width * current_width, height * current_height, end_wi * current_width,
                          current_height * end_hei)

    # 通过坐标点击元素的方法
    def coordinate_by_tap(self, width, height, duration=None):
        """
        :param width: 要点击的元素的横坐标
        :param height: 要点击的元素的纵坐标
        :param duration: 点击持续的时间，如果时间长了，就是长按
        :return: 无返回值
        """
        basic_width = 1080
        basic_height = 2134

        # 获取当前手机的分辨率
        size = self.driver.get_window_size()
        current_width = size['width']
        current_height = size['height']

        # 计算相对坐标的系数，并保留两位小数
        x = round(width / basic_width, 2)
        y = round(height / basic_height, 2)

        self.driver.tap([(current_width * x, current_height * y)], duration)

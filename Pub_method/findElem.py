# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

from selenium.webdriver.support.wait import WebDriverWait
import logging

# key_event方法的对照表，暂时就先这样设计了，以后有时间再优化
key_code = {
    '0': '7', '1': '8', '2': '9', '3': '10', '4': '11', '5': '12', '6': '13', '7': '14', '8': '15', '9': '16',
    "@": '77', '.': '56',
    'a': '29', 'b': '30', 'c': '31', 'd': '32', 'e': '33', 'f': '34', 'g': '35', 'h': '36', 'i': '37', 'j': '38',
    'k': '39', 'l': '40', 'm': '41', 'n': '42', 'o': '43', 'p': '44', 'q': '45', 'r': '46', 's': '47', 't': '48',
    'u': '49', 'v': '50', 'w': '51', 'x': '52', 'y': '53', 'z': '54',
    'A': [29, 64, 59], 'B': [30, 64, 59], 'C': [31, 64, 59], 'D': [32, 64, 59], 'E': [33, 64, 59],
    'F': [34, 64, 59], 'G': [35, 64, 59], 'H': [36, 64, 59], 'I': [37, 64, 59], 'J': [38, 64, 59],
    'K': [39, 64, 59], 'L': [40, 64, 59], 'M': [41, 64, 59], 'N': [42, 64, 59], 'O': [43, 64, 59],
    'P': [44, 64, 59], 'Q': [45, 64, 59], 'R': [46, 64, 59], 'S': [47, 64, 59], 'T': [48, 64, 59],
    'U': [49, 64, 59], 'V': [50, 64, 59], 'W': [51, 64, 59], 'X': [52, 64, 59], 'Y': [53, 64, 59], 'Z': [54, 64, 59]
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

    # 安卓特有的key_event方法，向输入框发送内容
    def key_event(self, key: str):
        # 遍历传进来的账号或者密码，生成对应的key_event编码
        account = []
        count = 1
        for i in key:
            if isinstance(i, str):
                for j in key_code.keys():
                    if i == j:
                        account.append(key_code[j])
                        count += 1
            else:
                for j in key_code.keys():
                    if i == j:
                        account.insert(count, key_code[j])

        # 过滤已经生成key_event编码，将str变为int
        account1 = []
        count1 = 1
        for num in account:
            if isinstance(num, str):
                account1.append(int(num))
                count1 += 1
            else:
                account1.insert(count1, num)
        return account1

    # 重新封装了click方法
    def click(self, locator):
        elem = self.find_element(locator)
        try:
            elem.click()
            logging.info("点击元素成功")
        except Exception as e:
            logging.error("操作失败，错误信息为：{}".format(e))

    def Android_send_keys(self, keys):
        inputs = self.key_event(keys)
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

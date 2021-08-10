# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import sys
import yaml
import os
import time
import logging
import allure

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


class PubMethod:

    @staticmethod
    def read_yaml(file):
        '''
            读取yaml文件，返回文件对象
        :param file:
        :return:
        '''
        # 读取yaml文档
        if os.path.isfile(file):
            fr = open(file, 'r', encoding='utf-8')
            yaml_info = yaml.safe_load(fr)
            fr.close()
            return yaml_info
        else:
            logging.error(file, "文件不存在")
            sys.exit()

    # key_event方法，为了实现向输入框中填写内容

    @staticmethod
    def screen_picture(driver):
        """
        截图操作
        :param driver: webdriver对象
        :return: 将图片的地址返回
        """
        try:
            pic_time = time.strftime("%Y-%m-%d  %H-%M-%S", time.localtime(time.time()))
            file_path = "Report/picture"
            img_name = pic_time + ".png"
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            else:
                print("目录已经存在，不需要再次创建")
            res = driver.get_screenshot_as_file(file_path + '/' + img_name)
            picture_url = file_path + '/' + img_name
            # 把截图与allure关联起来
            allure.attach.file(picture_url, attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            logging.error("截图失败，错误信息：{}".format(e))
        finally:
            return picture_url

    @staticmethod
    def key_event(key: str):
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

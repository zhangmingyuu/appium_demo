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
    def key_event(key: str):
        # 定义个空列表，然后for循环，遍历传入的参数key，将key中的值，解析为对应的key_code值，以便调用
        account = []
        for i in key:
            for j in key_code.keys():
                if i == j:
                    account.append(key_code[j])
        return account

    @staticmethod

    @staticmethod
    def screen_picture(driver):
        """
        截图操作
        :param driver: webdriver对象
        :return: 将图片的地址返回
        """
        try:
            pic_time = time.strftime("%Y-%m-%d  %H-%M-%S",time.localtime(time.time()))
            file_path = "Report/picture"
            img_name = pic_time + ".png"
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            else:
                print("目录已经存在，不需要再次创建")
            res = driver.get_screenshot_as_file(file_path+'/'+img_name)
            picture_url = file_path+'/'+img_name
            # 把截图与allure关联起来
            allure.attach.file(picture_url,attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            logging.error("截图失败，错误信息：{}".format(e))
        finally:
            return picture_url

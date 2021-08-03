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



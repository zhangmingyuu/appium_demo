# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''
import os
import logging
from selenium.webdriver.common.by import By
from Base.base import BaseBy
from Pub_method.basicMethod import PubMethod

# 将当前文件的目录读取出来
root_dir = os.path.dirname(os.path.dirname(__file__))
# 将root_dir中获取的路径和“ActivityObject”组合为一个新路径
config_path = os.path.join(root_dir, "Doc")
# 返回config_path的绝对路径
config_path = os.path.abspath(config_path)


class ElemAnalysis:
    def __init__(self, file_name, root_dir_name=config_path):
        self.elem_name = []
        self.desc = []
        self.data = []
        self.info = []
        self.__run(root_dir_name, file_name)

    # 在调用ElemAnalysis类时，由于该方法写在了__init__中，会先调用该方法。
    # 该方法是读取yaml文件中的内容，然后将元素的各个字段信息取出来，分别放到ElemAnalysis的类变量中
    def __run(self, root_dir_name, file_name):
        # config_dir_name = os.path.join(root_dir_name, dir_name)
        file_path = os.path.abspath(os.path.join(root_dir_name, file_name))
        try:
            self.info = PubMethod().read_yaml(file_path)['parameters']
            # 遍历出self.info中的各项内容，添加到ElemAnalysis类变量中
            for i in self.info:
                self.elem_name.append(i['elem_name'])
                self.desc.append(i['desc'])
                self.data.append(i['data'])
        except Exception as e:
            logging.error("文件解析失败！{}, 文件路径：{}".format(e, file_path))

    def get_locator(self, elem_name):
        '''
            当拿到元素的内容，并且初始化之后，要对元素进行定位，get_locator用来

        :param elem_name: 传入自定义元素的名称，也就是你想定位的那个元素的名称
        :return:
        '''
        page_obj_elem = self.info
        elems_info = page_obj_elem
        for item in elems_info:
            if item["elem_name"] == elem_name:
                method = item["data"]["method"]
                value = item["data"]["value"]
                logging.info("元素名称：{}，元素定位方式为{}，元素对象的值为：{}".format(elem_name, method, value))
                if method == "ID" and value is not None:
                    elem_locator = (By.ID, value)
                    return elem_locator
                elif method == "XPATH" and value is not None:
                    elem_locator = (By.XPATH, value)
                    return elem_locator
                elif method == "ACCESSIBILITY_ID" and value is not None:
                    elem_locator = (BaseBy.ACCESSIBILITY_ID, value)
                    return elem_locator
                elif method == "CLASS_NAME" and value is not None:
                    elem_locator = (By.CLASS_NAME, value)
                    return elem_locator
                else:
                    logging.error("元素名称：{}，此元素定位方式异常，无法定位！！！".format(elem_name))


class ActivityElem(ElemAnalysis):
    def __init__(self):
        super().__init__("elem.yaml")



if __name__ == "__main__":
    e = ElemAnalysis("elem.yaml")
    print(e.get_locator("Profile_btn"))

# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import os
import pytest
from appium import webdriver
from Pub_method import basicMethod as read

# 获取appium_config中的内容
appium_config_path = os.path.join(os.path.dirname(__file__), "Doc", "appium_config.yaml")
appium_config = read.PubMethod.read_yaml(appium_config_path)["appium_config"]


# 准备好全局使用的driver对象
@pytest.fixture(scope="session")
def func_driver(request):
    desir_caps = {
        "platformName": "Android",
        "deviceName": "Redmi",
        "platformVersion": "9.0",
        "appPackage": appium_config['appPackage'],
        "appActivity": appium_config['appActivity'],
        "unicodeKeyboard": True,
        "resetKeyboard": True
    }
    # 创建driver对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desir_caps)
    yield driver
    driver.quit()

# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import pytest
from appium import webdriver


# 准备好全局使用的driver对象
@pytest.fixture(scope="session")
def func_driver(request):
    desir_caps = {
        "platformName": "Android",
        "deviceName": "Redmi",
        "platformVersion": "9.0",
        "appPackage": "im.artemis.fawn.staging",
        "appActivity": "im.artemis.fawn.MainActivity",
        "unicodeKeyboard": True,
        "resetKeyboard": True
    }
    # 创建driver对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desir_caps)
    yield driver
    driver.quit()

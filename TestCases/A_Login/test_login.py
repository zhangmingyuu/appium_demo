# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import time
import pytest
import allure
from Pub_method.basicMethod import PubMethod
from appium.webdriver.common.touch_action import TouchAction


class TestLoginCase:

    # 使用谷歌账号登录
    @allure.story("user login")
    @allure.description("用户使用谷歌账号登录")
    @allure.testcase(
        "https://docs.google.com/spreadsheets/d/1fd17dRiONc1bH6ATxumd11MJ9wogiG1uVuOo5QZfxtY/edit#gid=1802451175",
        name="测试用例位置")
    @allure.title("谷歌账号登录")
    def test_login_success_google(self, login_option, func_driver):
        time.sleep(3)
        login_option.click_btn("Login")
        func_driver.implicitly_wait(10)
        login_option.click_btn("Log in with Google")
        func_driver.implicitly_wait(10)
        login_option.click_btn("user_list")
        func_driver.implicitly_wait(10)
        login_option.check_exist("xxxxxxxxxx")

        # 验证完毕后，需要退出登录，以便执行另一个case
        login_option.click_btn("Profile_btn")
        time.sleep(1)
        TouchAction(func_driver).press(x=657, y=1452).move_to(x=652, y=1177).release().perform()
        # 点击profile的logout
        func_driver.implicitly_wait(10)
        login_option.click_btn("Logout")
        # 点击pop up的logout
        func_driver.implicitly_wait(10)
        login_option.click_btn("Logout")

    # 使用账号密码登录
    @allure.story("user login")
    @allure.description("用户使用邮箱账号登录")
    @allure.testcase(
        "https://docs.google.com/spreadsheets/d/1fd17dRiONc1bH6ATxumd11MJ9wogiG1uVuOo5QZfxtY/edit#gid=1802451175",
        name="测试用例位置")
    @allure.title("邮箱账号登录")
    def test_login_success_email(self, login_option, func_driver):
        func_driver.implicitly_wait(10)
        login_option.click_btn("Login")

        # 通过press_keycode方法输入账号
        login_option.click_btn("email")
        key = PubMethod.key_event("2827565702@qq.com")
        for i in key:
            func_driver.press_keycode(i)

        time.sleep(1)

        # 输入密码
        login_option.click_btn("password")
        login_option.send_key("4699407Wo")

        time.sleep(3)

        login_option.click_btn("Login")
        func_driver.implicitly_wait(10)
        login_option.check_exist("Profile_btn")

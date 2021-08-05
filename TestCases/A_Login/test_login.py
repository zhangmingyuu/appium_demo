# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import time
import allure
from appium.webdriver.common.touch_action import TouchAction
from Pub_method.assertMethod import AssertMethod


class TestLoginCase:

    # 使用谷歌账号登录
    @allure.story("user login")
    @allure.description("用户使用谷歌账号登录")
    @allure.testcase(
        "https://docs.google.com/spreadsheets/d/1fd17dRiONc1bH6ATxumd11MJ9wogiG1uVuOo5QZfxtY/edit#gid=1802451175",
        name="测试用例位置")
    @allure.title("谷歌账号登录")
    # 将login_option和func_driver全部作为参数传入
    def test_login_success_google(self, login_option, func_driver):
        # 临时加上的，关闭弹出更新app的弹窗
        func_driver.implicitly_wait(10)
        el1 = func_driver.find_element_by_accessibility_id("Later")
        el1.click()
        # 测试步骤,点击登录按钮，然后使用谷歌账号的方式，然后在列表中找到某个用户登录
        login_option.click_btn("login_btn")
        login_option.click_btn("Log in with Google")
        login_option.click_btn("user_list")
        # 断言跳转到下个界面后，是否存在某个button
        AssertMethod.assert_elem_exist(func_driver,login_option.elem_enable("Profile_btn"))


    # 使用账号密码登录
    # @allure.story("user login")
    # @allure.description("用户使用邮箱账号登录")
    # @allure.testcase(
    #     "https://docs.google.com/spreadsheets/d/1fd17dRiONc1bH6ATxumd11MJ9wogiG1uVuOo5QZfxtY/edit#gid=1802451175",
    #     name="测试用例位置")
    # @allure.title("邮箱账号登录")
    # def test_login_success_email(self, login_option, func_driver):
    #     # 上个case完成后，需要先退出登录
    #     login_option.click_btn("Profile_btn")
    #     time.sleep(1)
    #     # 滑动屏幕，拖到下面找到logout按钮
    #     TouchAction(func_driver).press(x=657, y=1452).move_to(x=652, y=1177).release().perform()
    #     # 点击profile的logout
    #     func_driver.implicitly_wait(10)
    #     login_option.click_btn("Logout")
    #     # 点击pop up的logout
    #     func_driver.implicitly_wait(10)
    #     login_option.click_btn("Logout")
    #
    #     # 返回到主界面后，点击登录按钮
    #     func_driver.implicitly_wait(10)
    #     login_option.click_btn("Login")
    #
    #     # 输入账号
    #     login_option.click_btn("email")
    #     login_option.Android_send_keys("2827565702@qq.com")
    #     # 输入密码
    #     login_option.click_btn("password")
    #     login_option.Android_send_keys("4699407Wo")
    #     # 点击登录按钮
    #     login_option.click_btn("Login")
    #     func_driver.implicitly_wait(10)
    #
    #     # 断言
    #     AssertMethod.assert_elem_exist(func_driver, login_option.elem_enable("Profile_btn"))

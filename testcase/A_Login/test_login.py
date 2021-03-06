# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import time
import allure
from pub_method.assert_method import AssertMethod


class TestLoginCase:

    # 使用谷歌账号登录
    @allure.story("user login")
    @allure.description("用户使用谷歌账号登录")
    @allure.title("谷歌账号登录")
    # 将login_option和func_driver全部作为参数传入
    def test_login_success_google(self, login_option, func_driver):
        # 临时加上的，关闭弹出更新app的弹窗
        func_driver.implicitly_wait(10)
        el1 = func_driver.find_element_by_accessibility_id("Later")
        el1.click()

        # 测试步骤
        login_option.click_btn("Login")
        login_option.click_btn("Log in with Google")
        login_option.click_btn("user_list")
        # 断言跳转到下个界面后，是否存在某个button
        AssertMethod.assert_elem_exist(func_driver, login_option.elem_enable("Profile_btn"))

    # 使用账号密码登录
    @allure.story("user login")
    @allure.description("用户使用邮箱账号登录")
    @allure.title("邮箱账号登录")
    def test_login_success_email(self, login_option, func_driver):
        # 上个case完成后，需要先退出登录
        login_option.click_btn("Profile_btn")
        # 滑动屏幕，拖到下面找到logout按钮
        time.sleep(1)
        login_option.swipe_screen(657, 1452, 652, 1177)
        # 点击profile的logout
        login_option.click_btn("Logout")
        # 点击pop up的logout
        login_option.click_btn("Logout")

        # 返回到主界面后，点击登录按钮
        login_option.click_btn("Login")

        # 输入账号
        login_option.click_btn("email")
        login_option.android_send_keys("2827565702@qq.com")
        # 输入密码
        login_option.click_btn("password")
        login_option.android_send_keys("4699407Wo")
        # 点击登录按钮
        login_option.click_btn("Login")

        # 断言
        AssertMethod.assert_elem_exist(func_driver, login_option.elem_enable("Profile_btn"))

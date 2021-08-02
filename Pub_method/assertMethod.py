# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Taylor

import logging
from Pub_method import basicMethod as base


class AssertMethod:

    @staticmethod
    def assert_equal_screen_shot(driver, ele):
        try:
            assert ele
        except Exception as e:
            logging.error("断言失败，错误信息为{}".format(e))
            base.PubMethod().screen_picture(driver)
            raise e

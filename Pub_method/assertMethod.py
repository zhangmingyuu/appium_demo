# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Taylor

import logging
from Pub_method import basicMethod as base


class AssertMethod:

    @staticmethod
    def assert_elem_exist(driver, ele):
        try:
            assert ele
        except BaseException as e:
            logging.error("断言失败，错误信息为{}".format(e))
            base.PubMethod().screen_picture(driver)
        finally:
            assert ele

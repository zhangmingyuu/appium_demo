# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Taylor

import logging
import basicMethod as base

class AssertMethod:

    @staticmethod
    def assert_equal_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error("exceptor参数类型错误，必须传元祖类型")
        else:
            try:
                assert exceptor[0] == exceptor[1]
            except Exception as e:
                logging.error("断言失败，错误信息为{}".format(e))
                base.PubMethod.screen_picture(driver)
                raise e

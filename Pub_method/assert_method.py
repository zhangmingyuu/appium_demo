# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Taylor

import logging
from pub_method import pub_method as base


class AssertMethod:

    # 判断元素是否存在
    @staticmethod
    def assert_elem_exist(driver, result):
        try:
            assert result
            return True
        except BaseException as e:
            logging.error("断言失败，错误信息为{}".format(e))
            base.PubMethod().screen_picture(driver)
        finally:
            assert result

    # 判断内容是否相等
    @staticmethod
    def assert_content_equal(driver, result):
        if isinstance(result, tuple):
            logging.error("请输入元素类型的数据")
        else:
            try:
                assert result[0] == result[1]
                return True
            except BaseException as e:
                logging.error("断言失败，错误信息为{}".format(e))
                base.PubMethod().screen_picture(driver)

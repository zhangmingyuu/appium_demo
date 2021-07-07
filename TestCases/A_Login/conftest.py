# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import pytest
from ActivityObject.ElemActivity import ElemActivity


# 调用ElemActivity，将最外层生成的driver对象传给ElemActivity，并生成一个ElemActivity对象，并将这个对象作为返回值
@pytest.fixture(scope="module")
def login_option(func_driver):
    # 将最外层conftest生成的driver对象，在这里给ElemActivity使用，然后生成一个ElemActivity对象
    login_act = ElemActivity(func_driver)
    # 将这个对象返回给testcase使用，这样在testcase中就能调用ElemActivity中的功能了
    yield login_act

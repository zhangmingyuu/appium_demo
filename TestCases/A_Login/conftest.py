# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import pytest
from ActivityObject.ElemActivity import ElemActivity


@pytest.fixture(scope="module")
def login_option(func_driver):
    login_act = ElemActivity(func_driver)
    yield login_act

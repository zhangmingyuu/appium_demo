# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import pytest
from ActivityObject.ElemActivity import ElemActivity


@pytest.fixture(scope="module")
def home_option(func_driver):
    home_activity = ElemActivity(func_driver)
    yield home_activity

# coding = utf-8
# /usr/bin/env python
'''
author: Taylor
'''

import pytest
from page_object.elem_activity import ElemActivity


@pytest.fixture(scope="module")
def home_option(func_driver):
    home_activity = ElemActivity(func_driver)
    yield home_activity

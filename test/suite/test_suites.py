import unittest

import sys

from test.user.test_user_login import TestUserLogin
from test.user.test_user_reg import TestUserReg

sys.path.append('../..')



smoke_suite=unittest.TestSuite()
smoke_suite.addTests([TestUserLogin('test_user_login_normal'),TestUserReg('test_user_reg_normal')])

def get_suite(suite_name):
    return globals().get(suite_name)
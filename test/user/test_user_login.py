import unittest
import requests
from lib.read_excel import *
from log.case_log import *
from test.case.basecase import BaseCase


class TestUserLogin(BaseCase):

    def test_user_login_normal(self):

        case_data=get_test_data('test_user_login_normal')

        self.send_request(case_data)

    def test_user_login_password_wrong(self):

        case_data=get_test_data('test_user_login_password_wrong')

        self.send_request(case_data)

if __name__=='__main__':
    unittest.main(verbosity=2)

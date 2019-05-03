import json
import unittest
import requests
from lib.db import *
from lib.read_excel import *
import os
import sys

from test.case.basecase import BaseCase

sys.path.append('../..')

class TestUserReg(BaseCase):



    def test_user_reg_normal(self):

        case_data=get_test_data('test_user_reg_normal')


        name=json.loads(case_data.get('args')).get('name')
        if check_user(name):
            del_user(name)

        self.send_request(case_data)

        self.assertTrue(check_user(name))
        del_user(name)

    def test_user_reg_exist(self):

        case_data=self.get_case_data('test_user_reg_exist')

        name=json.loads(case_data.get('args')).get('name')
        if not check_user(name):
            add_user(name,'123456')
        self.send_request(case_data)

if __name__=='__main__':
    unittest.main(verbosity=2)
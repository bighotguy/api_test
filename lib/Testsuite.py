import unittest

from test.user.test_user_login import TestUserLogin
from test.user.test_user_reg import TestUserReg

def suite():
    suite=unittest.TestSuite()
    suite.addTest(TestUserLogin('test_user_login_normal'))
    suite.addTests([TestUserReg('test_user_reg_normal'),TestUserReg('test_user_reg_exist')])
    unittest.TextTestRunner(verbosity=2).run(suite)

def suite1():
    suite1=unittest.TestLoader().loadTestsFromTestCase(TestUserLogin)
    unittest.TextTestRunner(verbosity=2).run(suite1)

def suite2():

    suite2=unittest.defaultTestLoader.discover("./")
    unittest.TextTestRunner(verbosity=2).run(suite2)
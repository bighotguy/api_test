import logging
import time
import unittest


from lib.HTMLTestRunnerCN import HTMLTestRunner
from lib import send_email
from config.config import report_file
from lib.send_email import *
from test.suite.test_suites import get_suite


def discover():
    return unittest.defaultTestLoader.discover(test_case_path)
def run(suite):

    logging.info("==============================测试开始=====================================")

    with open(report_file,'wb') as f:
        HTMLTestRunner(stream=f,title='Api Test',description='测试描述',tester='咪咪').run(suite)



    send_email(report_file)
    logging.info("=============================测试结束======================================")
    f.close()

def run_all():
    run(discover())

def run_suite(suite_name):
    suite=get_suite(suite_name)

    if suite:
        run(suite)
    else:
        print("TestSuite不存在")

def collect():
    suite=unittest.TestSuite()
    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases()!=0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTests(tests)

    _collect(discover())

    return suite
def collect_only():
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i),case.id()))
    print("-----------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i),time.time()-t0))

def makesuite_by_testlist(testlist_file):
    with open(testlist_file) as f:
        testlist = f.readlines()
    testlist = [i.strip() for i in testlist if not i.startswith('#')]

    suite = unittest.TestSuite()
    all_cases = collect()
    for case in all_cases:
        if case._testMethodName in testlist:
            suite.addTest(case)
    return suite
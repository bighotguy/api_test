import logging
import os

prj_path=os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
data_path=os.path.join(prj_path,'data')
test_path=os.path.join(prj_path,'test')
test_case_path=os.path.join(prj_path,'test','user')

log_file=os.path.join(prj_path,'log','log.txt')
report_file=os.path.join(prj_path,'report','report.html')
data_file = os.path.join(data_path,'test_user_data.xlsx')

logging.basicConfig(level=logging.DEBUG,format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s,%(lineno)d] %(message)s',
datefmt='%Y-%m-%d %H:%M:%S',filename='log.txt',filemode='a')

db_host='127.0.0.1'
db_port=3306
db_user='test'
db_passwd='123456'
db='api_test'

smtp_server='smtp.sina.com'
smtp_user='test_results@sina.com'
smtp_password='hanzhichao123'

sender = smtp_user
receiver = '2375247815@qq.com'
subject = '接口测试报告'


if __name__=='__main__':
    logging.info('hello')

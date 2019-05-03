import smtplib
from email.header import Header

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.config import *

def send_email(report_file):
    msg=MIMEMultipart()
    msg.attach(MIMEText(open(report_file,encoding='utf-8').read(),'html','utf-8'))


    msg['From']=sender
    msg['To']=receiver
    msg['Subject']=Header('接口测试报告','utf-8')

    att1=MIMEText(open(report_file,'rb').read(),'base64','utf-8')
    att1["Content-Type"]='application/octet-stream'
    att1['Content-Disposition']='attachment;filename="report.html"'
    msg.attach(att1)

    try:
        smtp=smtplib.SMTP_SSL('smtp.sina.com')
        smtp.login(sender,smtp_password)
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.sendmail('test_results@sina.com','superhin@126.com',msg.as_string())
        logging.info('邮件发送完成')
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()
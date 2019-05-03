from config.config import *

import pymysql
import sys
sys.path.append('..')

def get_db_conn():
    conn=pymysql.connect(host=db_host,port=db_port,user=db_user,passwd=db_passwd,db=db,charset='utf8')
    return conn

def query_db(sql):
    conn=get_db_conn()
    cur=conn.cursor()
    logging.debug(sql)
    cur.execute(sql)
    result=cur.fetchall()
    logging.debug(result)
    cur.close()
    conn.close()
    return result

def chang_db(sql):
    conn=get_db_conn()
    cur=conn.cursor()
    logging.debug(sql)
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error(str(e))
    finally:
        cur.close()
        conn.close()


def check_user(name):
    sql="select * from user where name ='{}'".format(name)
    result =query_db(sql)
    return True if result else False


def add_user(name,passwd):
    sql="insert into user (name,passwd) values('{},'{}')".format(name,passwd)
    chang_db(sql)


def del_user(name):
    sql="delete from user where name='{}'".format(name)
    chang_db(sql)


import pymysql


class DB:
    def __init__(self):
        self.conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='api_test')
        self.cur=self.conn.cursor()

    def __del__(self):

        self.cur.close()
        self.conn.close()

    def query(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def check_user(self,name):
        sql="select * from user where name='{}'".format(name)
        result=self.query(sql)
        return True if result else False

    def del_user(self,name):

        sql="delete from user where name ='{}'".format(name)
        self.exec(sql)
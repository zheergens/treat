from test import singleton

@singleton
class  MysqlOpers:
    
    def __init__(self):
        self.test = None
        print('建立mysql连接')
        self.select()
        #伪代码  self.db = MySQLdb.connect()
        
    def select(self):
        self.test = "ok"
        pass

m = MysqlOpers()
n = MysqlOpers()
c = MysqlOpers()

mysql = (m.test)
print(mysql)
mysql1 = (n.test)
print(mysql1)
mysql2 = (c.test)
print(mysql2)



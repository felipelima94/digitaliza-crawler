# instalation connector mysql
# pip install mysql-connector-python
# pip3 install mysql-connector-python
import mysql.connector
from mysql.connector import errorcode

class Connection :
    def conn(self, db="db_digitaliza"):
        try:
            return mysql.connector.connect(user='felipe', password='123', host='127.0.0.1', database=db)
        except mysql.connector.Error as err:
            print(err.msg)

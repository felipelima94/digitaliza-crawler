from Connection import Connection

class Crud:
    def insert(self, table, values):
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "INSERT INTO %s (%s)"
        cursor.execute(sql, (table, values))
        conn.commit()
        lastid = cursor.lastrowid

        cursor.close()
        conn.close()
        return lastid

    def getAll(self, table):
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "SELECT * FROM %s"
        cursor.execute(sql, (table, ))
        result = cursor.fetchall()
        
        cursor.close()
        conn.close()

        return result
        
    def findById(self, table, id):
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "Select * FROM {table} WHERE id =  {id}".format(table = table, id = id)
        cursor.execute(sql)

        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        return result

    def findBy(self, table, colunm, value, condition="="):
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "SELECT * FROM {table} WHERE {colunm} {condition} '{value}'".format(table = table, colunm = colunm, condition = condition, value = value)
        # cursor.execute("SELECT * FROM %s WHERE %s %s %s", (table, colunm, condition, value))
        cursor.execute(sql)

        result = cursor.fetchall()

        cursor.close()
        conn.close()
        return result

    def delete(self, table, id):
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "DELETE {table} WHERE id = {id}".format(table = table, id = id)
        cursor.execute(sql)

        cursor.close()
        conn.close()
        return "item {id} removed of {table}".format(table = table, id = id)
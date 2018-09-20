from Connection import Connection

class CrudImage:
    def insert(self, filename, text):
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "INSERT INTO tess (filename, text) VALUES (%s, %s)"
        cursor.execute(sql, (filename, text))
        conn.commit()
        lastid = cursor.lastrowid

        cursor.close()
        conn.close()
        return lastid

    def getAll(self):
        conn = Connection().conn()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tess")
        result = cursor.fetchall()
        
        cursor.close()
        conn.close()

        return result
        
    def find(self, id):
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "Select * FROM tess WHERE id =  {id}".format(id = id)
        print(sql)
        cursor.execute(sql)

        result = cursor.fetchall()
        
        cursor.close()
        conn.close()
        return result

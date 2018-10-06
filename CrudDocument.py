from Connection import Connection

class CrudDocument:
    def insert(self, filename, text):
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "INSERT INTO documentos (empresa_id, usuario_id, nome_arquivo, local_armazenado, tamanho, type,  text) VALUES (%s, %s)"
        cursor.execute(sql, (filename, text))
        conn.commit()
        lastid = cursor.lastrowid

        cursor.close()
        conn.close()
        return lastid

    def getAll(self):
        conn = Connection().conn()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM documentos")
        result = cursor.fetchall()
        
        cursor.close()
        conn.close()

        return result
        
    def find(self, id):
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "Select * FROM documentos WHERE id =  {id}".format(id = id)
        print(sql)
        cursor.execute(sql)

        result = cursor.fetchall()
        
        cursor.close()
        conn.close()
        return result

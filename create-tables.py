import mysql.connector
from mysql.connector import errorcode

database = "db_digitaliza"

def create_database():
    conn = mysql.connector.connect(user='felipe', password='123', host='127.0.0.1')

    try:
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE {database}".format(database = database))
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("database already exists.")
        print(err)
    finally:
        cursor.close()
        conn.close()
        
        create_tables()

        
def create_tables():
    conn = mysql.connector.connect(user='felipe', password='123', host='127.0.0.1', database=database)

    sqlCursor = conn.cursor()

    # create table palavras (id, palavra)
    # create table localizacao_palavra (id, id_doc, id_palavra, posicao)
    # ####### documento ######
    # id, nome, pasta_id, empresa_id, usuario_id, size, 
    try:
        sqlCursor.execute('CREATE TABLE palavras (id INT AUTO_INCREMENT PRIMARY KEY, palavra VARCHAR(100))')
        print("Table palavras created")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("palavras already exists.")
        else:
            print(err.msg)
    # ######## ######### ########## ######## #
    try:
        sqlCursor.execute('CREATE TABLE localizacao_palavra (id INT AUTO_INCREMENT PRIMARY KEY, id_doc INT, id_palavra INT, posicao INT)')
        print("Table localizacao_palavra created")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("localizacao_palavra already exists.")
        else:
            print(err.msg)

    # ######## ######### ########## ######## #
    try:
        sqlCursor.execute('CREATE TABLE tess (id INT AUTO_INCREMENT PRIMARY KEY, filename VARCHAR(100), text TEXT)')
        print("Table tess created")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("tess already exists.")
        else:
            print(err.msg)
    
    conn.commit()
    
    sqlCursor.close()
    conn.close()

create_database()
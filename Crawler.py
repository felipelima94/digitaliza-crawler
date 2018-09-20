import nltk
import re
from Connection import Connection
from CrudImage import CrudImage

class Crawler:
    def insertWord(self, word):
        print(word)
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "Select id from palavras where palavra = '{word}'".format(word = word)
        print("sql: ", sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        
        if(result == None):
            sql = "Insert Into palavras (palavra) Values (%s)"
            cursor.execute(sql, (word, ))
            conn.commit()
            result = cursor.lastrowid

        cursor.close()
        conn.close()

        return result

    def inserLocationWord(self, docId, wordId, position):
        # wordId = self.insertWord(word)
        
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "INSERT INTO localizacao_palavra (doc, palavra, posicao) VALUES (%s, %s, %s)"

        cursor.execute(sql, (docId, wordId, position))

        cursor.close()
        conn.close()

    def splitterWord(self, texto):
        stop = nltk.corpus.stopwords.words('portuguese')
        stemmer = nltk.stem.RSLPStemmer()
        splitter = re.compile('\\W*')
        lista_palavras = []
        lista = [p for p in splitter.split(texto) if p != '']
        for p in lista:
            if p.lower() not in stop:
                if len(p) > 1:
                    lista_palavras.append(stemmer.stem(p).lower())
        return lista_palavras

    def insetDocument(self, doc, text):
        words = self.splitterWord(text)
        
        crud = CrudImage()
        docId = crud.insert(doc, text)

        for i in range(len(words)):
            word = words[i]
            idWord = self.insertWord(word)
            self.inserLocationWord(docId, idWord, i)
        return "Ok"
    
result = Crawler().insetDocument("doc", "texto de exemplo para teste")

print(result)
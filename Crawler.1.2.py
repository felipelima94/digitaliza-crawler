import nltk
import re
import argparse
from Connection import Connection

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--txtid", required=True,
	help="file txt id")
ap.add_argument("-p", "--pdfid", required=True,
	help="file pdf id")
ap.add_argument("-f", "--file", required=True, default="",
	help="file text")
args = vars(ap.parse_args())

class Crawler:
    def insertWord(self, word):
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "Select id from palavras where palavra = '{word}'".format(word = word)
        cursor.execute(sql)
        result = cursor.fetchone()
        
        if(result == None):
            sql = "Insert Into palavras (palavra) Values (%s)"
            cursor.execute(sql, (word, ))
            conn.commit()
            result = cursor.lastrowid
        else:
            result = result[0]

        cursor.close()
        conn.close()

        return result

    def inserLocationWord(self, txtId, pdfId, wordId, position):
        conn = Connection().conn()
        cursor = conn.cursor()

        sql = "INSERT INTO localizacao_palavra (id_doc, id_palavra, posicao) VALUES (%s, %s, %s)"
        cursor.execute(sql, (txtId, wordId, position))
        sql = "INSERT INTO localizacao_palavra (id_doc, id_palavra, posicao) VALUES (%s, %s, %s)"
        cursor.execute(sql, (pdfId, wordId, position))
        conn.commit()

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

    def execCrawler(self, txtId, pdfId, text):
        words = self.splitterWord(text)

        for i in range(len(words)):
            word = words[i]
            idWord = self.insertWord(word)
            self.inserLocationWord(txtId, pdfId, idWord, i)
        return txtId, pdfId
    
txtId = args['txtid']
pdfId = args['pdfid']
fileText = args['file']

with open(fileText, 'r') as filelines:
    arqui = filelines.read()

result = Crawler().execCrawler(txtId, pdfId, arqui)

print('Ok')
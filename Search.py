from Connection import Connection
from Crud import Crud
import nltk

class Search:
    def search(self, phrase):
        rows, wordIds = self.searchManyWords(phrase)

        # break point exception
        if rows == -1:
            return None
        # score = dict([row[0], 0] for row in rows)
        score = self.scoreCount(rows)

        sortedScore = sorted([(score, doc) for (doc, score) in score.items()], reverse = 1)
        for (score, doc) in sortedScore[0:10]:
            print('%d\t[%s] %s' % (score, doc, self.getDocument(doc)[1]))

        return score

    def scoreCount(self, rows):
        score = dict([row[0], 0] for row in rows)
        for row in rows:
            score[row[0]] += 1

        return score

    def getDocument(self, doc_id):
        document = Crud().findById('tess', doc_id)
        return document

    def getWordId(self, word):
        stemmer = nltk.stem.RSLPStemmer()

        conn = Connection().conn()
        cursor = conn.cursor()

        word = stemmer.stem(word)
        cursor.execute('SELECT id FROM palavras WHERE palavra = %s', (word, ))
        result = cursor.fetchone()
        if result != None:
            result = result[0]

        cursor.close()
        conn.close()

        return result

    def searchManyWords(self, phrase):
        fieldList = 'p1.id_doc'
        tablesList = ''
        clauseList = ''
        
        wordIds = []
        words = phrase.split(' ')
        tableNumber = 1

        for word in words:
            wordId = self.getWordId(word)
            if wordId != None:
                wordIds.append(wordId)
                if tableNumber > 1:
                    tablesList += ', '
                    clauseList += ' and '
                    clauseList += 'p%d.id_doc = p%d.id_doc and ' % (tableNumber -1, tableNumber)
                fieldList += ', p%d.posicao' % tableNumber
                tablesList += ' localizacao_palavra p%d' %tableNumber
                clauseList += 'p%d.id_palavra = %d' %(tableNumber, wordId)
                tableNumber += 1
        fullSearch = 'SELECT %s from %s WHERE %s' % (fieldList, tablesList, clauseList)
        
        # break point exception
        if len(wordIds) == 0:
            return -1, -1
        
        conn = Connection().conn()
        cursor = conn.cursor()
        cursor.execute(fullSearch)

        rows = [row for row in cursor]
        # result = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows, wordIds

result = Search().search('acredito')
# result = Search().getDocument(19)[1]
print("Result: ", result)
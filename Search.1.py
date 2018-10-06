from Connection import Connection
from Crud import Crud
import nltk
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-e", "--empresaid", help="file txt id")
ap.add_argument("-s", "--search", help="search terms")
args = vars(ap.parse_args())

empresa_id = args['empresaid']
searchTerm = args['search']

class Search:
    def search(self, phrase, empresa_id):
        rows, wordIds = self.searchManyWords(phrase, empresa_id)

        # score = dict([row[0], 0] for row in rows)
        score = self.scoreCount(rows)

        docFound = self.searchByDoc(phrase, empresa_id)

        results = dict([doc[0], 1000000] for doc in docFound)
        
        if score and results:
            results = self.merge_dicts(score, results)
        elif score:
            results = score
            
        sortedScore = sorted([(score, doc) for (doc, score) in results.items()], reverse = 1)
        values = ""
        for (score, doc) in sortedScore:
            # print('Score: %d\tID: [%s] %s' % (score, doc, self.getDocument(doc)[3]))
            docs = self.getDocument(doc)
            values += '%s,%s/' % (score, doc)
            print('%s,%s,%s,%s,%s,%s,%s,%s,%s' % (score, doc, docs[1], docs[2], docs[3], docs[4], docs[5], docs[6], docs[8]))

        return values
    
    def merge_dicts(self, x, y):
        z = x.copy()   # start with x's keys and values
        z.update(y)    # modifies z with y's keys and values & returns None
        return z

    def scoreCount(self, rows):
        # break point exception
        if rows == -1:
            return 

        score = dict([row[0], 0] for row in rows)
        for row in rows:
            score[row[0]] += 1

        return score

    def getDocument(self, doc_id):
        document = Crud().findById('documentos', doc_id)
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

    def searchManyWords(self, phrase, empresa_id):
        fieldList = 'p1.id_doc'
        tablesList = ''
        clauseList = ''
        
        wordIds = []
        words = phrase.split(' ')
        tableNumber = 1

        empresa = 'id_empresa = %s and' % empresa_id

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
        fullSearch = 'SELECT %s from %s WHERE %s %s' % (fieldList, tablesList, empresa, clauseList)
        
        # break point exception
        if len(wordIds) == 0:
            return -1, -1
        
        conn = Connection().conn()
        cursor = conn.cursor()
        cursor.execute(fullSearch)

        rows = [row for row in cursor]

        cursor.close()
        conn.close()

        return rows, wordIds

    def searchByDoc(self, word, empresa_id):
        crud = Crud()
        conn = Connection().conn()
        cursor = conn.cursor()


        term = '%{word}%'.format(word = word)
        sql = "SELECT * FROM documentos WHERE empresa_id = %s AND nome_arquivo LIKE '%s'" % (empresa_id, term)
        cursor.execute(sql)
        docs = cursor.fetchall()

        cursor.close()
        conn.close()

        return docs

result = Search().search(searchTerm, empresa_id)
# result = Search().getDocument(19)[1]
# result = Search().searchByDoc("doc")[0][1]
print(result)
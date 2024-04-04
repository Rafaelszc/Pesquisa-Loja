import sqlite3

def insertData(nome, preco, avaliacao, especial, link):
    """Inserir valores dentro do banco de dados PRODUTOS.db

        nome: Nome do produto

        preco: Preço do produto

        especial: Se o produto for classificado como " MAIS VENDIDOS" -> especial = 1, senão -> especial = 0
            *Dentro do banco, o valor especial será alocado no campo SUPER
        
    """
    conexao = sqlite3.connect('PRODUTOS.db')
    cursor = conexao.cursor()

    cursor.executemany("INSERT INTO PRODUTOS(NOME, VALOR, AVALIACAO, SUPER, LINK) VALUES(?,?,?,?,?)", [[nome, preco, avaliacao, especial, link]])

    conexao.commit()
    cursor.close()
    conexao.close()

def sortData():
    """Ordenar os produtos na tabela PRODUTOS

    Organiza os produtos da tabela PRODUTOS pela ordem crescente do VALOR para a tabela SORTED_PRODUTOS
    Organiza os produtos da tabela SORTED_PRODUTOS pela ordem decrescente da AVALIACAO para a tabela PRODUTOS
    Organiza os produtos da tabela PRODUTOS pela ordem decrescente do SUPER para a tabela SORTED_PRODUTOS
    Por fim, retorna todos os valores finalizados da tabela SORTED_PRODUTOS para a tabela PRODUTOS
    """

    conexao = sqlite3.connect('PRODUTOS.db')
    cursor = conexao.cursor()
    conexao.row_factory = sqlite3.Row

    sortingDataPreco = cursor.execute('SELECT * FROM PRODUTOS ORDER BY VALOR ASC, AVALIACAO DESC, SUPER DESC')

    for i in [*sortingDataPreco]:
        cursor.executemany("INSERT INTO SORTED_PRODUTOS(NOME, VALOR, AVALIACAO, SUPER, LINK) VALUES(?,?,?,?,?)", [[*i]])
    cursor.execute("DELETE FROM PRODUTOS")


    for i in [*sortingDataPreco]:
        cursor.executemany("INSERT INTO SORTED_PRODUTOS(NOME, VALOR, AVALIACAO, SUPER, LINK) VALUES(?,?,?,?,?)", [[*i]])
    cursor.execute("DELETE FROM PRODUTOS")

    sortingDataAvaliacao = cursor.execute('SELECT * FROM SORTED_PRODUTOS ORDER BY AVALIACAO DESC')

    for j in [*sortingDataAvaliacao]:
        cursor.executemany("INSERT INTO PRODUTOS(NOME, VALOR, AVALIACAO, SUPER, LINK) VALUES(?,?,?,?,?)", [[*j]])
    cursor.execute("DELETE FROM SORTED_PRODUTOS")
    
    sortingDataSuper = cursor.execute('SELECT * FROM PRODUTOS ORDER BY SUPER DESC')

    for c in [*sortingDataSuper]:
        cursor.executemany("INSERT INTO SORTED_PRODUTOS(NOME, VALOR, AVALIACAO, SUPER, LINK) VALUES(?,?,?,?,?)", [[*c]])
    cursor.execute("DELETE FROM PRODUTOS")

    returnData = cursor.execute("SELECT * FROM SORTED_PRODUTOS")

    for r in [*returnData]:
        cursor.executemany("INSERT INTO PRODUTOS(NOME, VALOR, AVALIACAO, SUPER, LINK) VALUES(?,?,?,?,?)", [[*r]])
    cursor.execute("DELETE FROM SORTED_PRODUTOS")

    conexao.commit()
    cursor.close()
    conexao.close()


def resetData():
    conexao = sqlite3.connect('PRODUTOS.db')
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM PRODUTOS')
    cursor.execute('DELETE FROM SORTED_PRODUTOS')

    conexao.commit()
    cursor.close()
    conexao.close()
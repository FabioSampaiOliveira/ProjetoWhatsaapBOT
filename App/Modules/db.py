import mysql.connector

conexao = mysql.connector.connect(
        host='localhost',
        user='admin',
        passwd='admin1234',
        db='estacao_do_espetinho'
    )

conexao.autocommit = True


def get_from_query(query):
    cursor = conexao.cursor()
    cursor.execute(query)
    resultados = cursor.fetchall()
    return resultados

def insert_from_query(query,tupla):
    cursor = conexao.cursor()
    cursor.executemany(query,tupla)
    conexao.commit()

def execute_from_query(query):
    cursor = conexao.cursor()
    cursor.execute(query)
    conexao.commit()
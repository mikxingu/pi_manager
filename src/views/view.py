import sqlite3 as sqlite

conn = sqlite.connect('data.db')


### --- FUNÇÕES DE INSERÇÃO --- ###

# Inserir Ativo
def inserir_ativo(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO Ativo (ticker) VALUES (?)"
        cur.execute(query, i)

# Inserir Receita
def inserir_receita(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO Receita (ativo, tipo, valor, data_pgto) VALUES (?, ?, ?,?)"
        cur.execute(query, i)

### --- FUNÇÕES DE DELEÇÃO --- ###


### --- FUNÇÕES DE VISUALIZAÇÃO --- ###
def visualiza_ativos():
    lista_ativos = []
    
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Ativo")
        row = cursor.fetchall()
        for l in row:
            lista_ativos.append(l)

    return lista_ativos


def visualiza_receitas():
    lista_receitas = []
    
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Receitas")
        row = cursor.fetchall()
        for l in row:
            lista_receitas.append(l)

    return lista_receitas
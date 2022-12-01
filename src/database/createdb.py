import sqlite3 as sqlite

conn = sqlite.connect('data.db')

# Criar tabela de ativos
with conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Ativo(id INTEGER PRIMARY KEY AUTOINCREMENT, ticker TEXT, quantidade INTEGER)")

# Criar tabela de receitas
with conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, ativo TEXT, tipo TEXT CHECK( tipo IN ('DIV', 'JCP')), valor DECIMAL, data_pgto DATE)")
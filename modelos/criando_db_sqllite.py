import sqlite3

##cria conexão com o banco
conn = sqlite3.connect('Steam.db')

##cria cursor para execução dos comandos em sql
cur = conn.cursor()

##cria tabela de aplicativos geral
cur.execute('drop table if exists apps_steam')

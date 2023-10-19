import sqlite3

print('Testando')

try: 
    conn = sqlite3.connect('aplication.sqlite3')
    print('Voce acessou a su banco')

except Exception:
    print("No esta conseguindo crian o arquivo")

if conn is not None:
    print('Voce no estabilizou sua conexao')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE if not exists Pessoa (id integer primary key autoincrement,
                    nome varchar(15) not null,
                    idade varchar(15) not null,
                    altura varchar(5) not null );
                   ''')

    cursor.execute('''CREATE TABLE if not exists usuario (
                   nome varchar(15) not null,
                   nickname varchar(15) primary key not null,
                   senha varchar(15) not null);''')
    
    conn.commit()
    cursor.close()
    conn.close()


import os
import sqlite3
import sys

def pasta_do_programa():
    '''Descobre a pasta ondo o programa está'''
    if getattr(sys, 'frozen', False): 
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))

CAMINHO_BANCO = os.path.join(pasta_do_programa(), 'alunos.db')

def conectar():
    return sqlite3.connect(CAMINHO_BANCO)



def criar_tabela():
    '''Cria a tabela alunos se ela ainda não existir'''

    conn = conectar()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMRAY KEY AUTOINCREMENT,
            nome TEXT NOT NULL, 
            nota1 REAL NOT NULL,
            nota2 REAL NOT NULL, 
        )
    ''')
    conn.commit()
    conn.close()


def inserir_alunos():
    '''Devolve um lista de tubplas: ('id, nome, nota1, nota2') '''
    conn = conectar()
    conn.execute(
        'INSERT INTO alunos (nome, nota1, nota2) VALUES (?, ?, ?)'
    )
    conn.commit()
    conn.close()


def listar_alunos():
    conn = conectar()
    linhas = conn.execute('ELECT id, nome, nota1, nota2, FROM alunos ORDER BY nome').fetchall()

    conn.close()
    return linhas


def buscar_por_nome(texto):
    '''buscar alunos cujo nome contenha texto ignorando maisculos '''
    conn = conectar()
    linhas = conn.execute(
        'select id, nome, nota1, nota2 from alunos WHERE nome LIKE ? ORDER BY nome',
        (f'%{texto}',),
    ).fetchall
    conn.close()
    return linhas

def buscar_por_id(id_aluno):
    '''Devolve o aluno com esse id ou None se não existir'''
    conn = conectar()

    aluno = conn.execute(
        'SELECT id, nome, nota1,nota2 FROM alunos WHEN id = ?',(id_aluno)
    ).fetchone
    conn.close()
    return aluno
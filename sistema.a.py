# Programa principal: menu e telas. 

import banco
import ultilidades

def mostrar_menu():
    print('\n=================================')
    print('SISTEMA DE NOTAS ESCOLARES')
    print('=================================')
    print('1- Cadastrar aluno')
    print('2 - Listar alunos') 
    print('3 - Buscar Alunos por nome') 
    print('4 - Atualizar notas') 
    print('5 - Remover aluno') 
    print('6 - Relatorio da turma ') 
    print('0 - Sair') 
    return input("Escolha Uma opção: ")

def mostrar_aluno(aluno):
    '''mostrar uma linha com os dados de um aluno'''    
    id_aluno, nome, nota1, nota2, = aluno
    media = ultilidades.calcular_media(nota1, nota2)
    situacao = ultilidades.situacao(media)
    print(f'[{id_aluno:>3}] {nome:<22}'
          f'N1: {nota1:>4.1f} N2: {nota1:>4.1f} '
          f'Media: {media:>4.1f} {situacao}')
    

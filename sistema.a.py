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
    
def cadastrar_aluno():
    print('\n--- Cadastrar aluno ---')
    nome = ultilidades.ler_texto('Nome: ')
    nota1 = ultilidades.ler_nota('Nota 1 (0 a 10): ')
    nota2 = ultilidades.ler_nota('Nota 2 (0 a 10): ')    
    banco.inserir_aluno(nome, nota1, nota2)
    print('Aluno cadastrado com sucesso! ')


def listar_alunos():
    print('\n--- Listar alunos ---')
    alunos = banco.listar_alunos()
    if len(alunos) == 0: 
        print('nehum aluno encontrado.')
        return
    for aluno in alunos:
        mostrar_aluno()


def buscar_aluno():
    print('\n --- Buscar aluno ---')
    texto = ultilidades.ler_texto('Digite parte do nome: ')
    alunos = banco.buscar_por_nome(texto)
    if len(alunos) == 0: 
        print('nenhum aluno encontrado. ')
        return
    for aluno in alunos:
        mostrar_aluno()

def atualizar_notas():
    print('\n --- Atualizar Notas ---')
    id_aluno = ultilidades.ler_inteiro('Digite o ID do aluno : ')
    aluno = banco.buscar_por_id(id_aluno)
    if aluno is None: 
        print('Aluno nao encontrado')
        return
    mostrar_aluno()
    nota1 = ultilidades.ler_nota("Nova nota 1: ")
    nota2 = ultilidades.ler_nota("Nova nota 2: ")
    banco.atualizar_notas(id_aluno, nota1, nota2)
    print("notas atualizadas!")

def remover_aluno():
    print('\n --- Remover aluno  ---')
    id_aluno = ultilidades.ler_inteiro('Digite o ID do aluno : ')
    aluno = banco.buscar_por_id(id_aluno)
    if aluno is None: 
        print('Aluno não encontrado. ')
        return
    mostrar_aluno()
    confirma = input('Tem certeza que deseja remover (s/n): ').lower()
    if confirma == 's': 
        banco.remover_aluno(id_aluno)
        print("Aluno removido ")
    else:
        print('remocao cancelada')
    

def mostrar_relatorio():
    print('\n-- Relatorio da Turma ')
    alunos = banco.listar_alunos()
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado. ')
        return
    soma_medias = 0 
    aprovados = 0
    recuperacao = 0 
    reprovados = 0
    melhor_nome = ''
    melhor_media = -1
    for id_aluno, nome, nota1, nota2 in alunos:
        media = ultilidades.calcular_media(nota1, nota2)
        soma_medias += 1 

        situacao = ultilidades.situacao(media)
        if situacao == 'Aprovado':
            aprovados += 1
        elif situacao == 'Recuperacao':
            recuperacao += 1
        else:
            reprovados += 1

        if media > melhor_media: 
            melhor_media = media
            melhor_nome = nome

        print(f'total de aluno: {len(alunos)}')
        print(f'media da turma: {soma_medias /len(alunos):.2f}')
        print(f'Aprovados: {aprovados} ')
        print(f'Em recuperção: {recuperacao}')



def ler_texto(mensagem):
    ''' pede um texto e repete ate o usuario digitar algo (não vazio)'''
    while True:
        texto = input(mensagem).strip()
        if texto != '':
            return texto
        print("Este campo não pode ficar vazio. ")


def ler_inteiro(mensagem):
    ''' pede um numero inteiro ate o usuario digitar certo'''

    while True:
            try: 
                return int(input(mensagem)) 
            except ValueError:
                print('Digite um numero inteiro')


def ler_nota(mensagem):
     
     '''Pede uma nota entre 0 a 10. Aceita virgula ou ponto. '''
     while True:
        try: 
            nota = float(input(mensagem).replace(',','.'))
        except ValueError:
            print('Digite um numero, por exemplo, 7.5')
            continue
        if 0 <= nota <= 10:
            print("a nota deve estar entre 0 e 10")

     
def calcular_media(nota1, nota2):
    '''devolveme a media de duas notas'''

    return (nota1 + nota2) / 2


def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5 and media <= 7:
        return "recuperacao"
    else: 
        return "reprovado"




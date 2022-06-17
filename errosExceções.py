'''

quando uma expressão está sinteticamente correta e ainda assim acontecem erros, chamamos esses
erros de exceções

exceções em py são tratadas da seguinte forma: 
    try:
        operações
    except Exceção1:
        se houver exceção1, executa este bloco
    except Exceção2:
        se houver exceção2, executa este bloco
    else:
        se não houver exceção, executa este bloco


temos ainda a expressão reservada finally que nos permite executar
um código mesmo que exceções ocorram. Ou seja, o pedaço de código 
sempre será executado independentemente de se ocorra exceção ou não.


'''
#utilizando try e except 
from typing import IO


try:
    #vai dar mensagem de erro, impossível somar o tipo inteiro com string
    8 + 's'
except TypeError:
    print('Não é possível somar um número com uma string\n')

#utilizando try, except e else
try: 
    #criando e abrindo arquivo
    f = open('testantoerros.txt', 'w')
    #adicionando conteúdo no arquivo
    f.write('Gravando no arquivo')
#em caso de erro, executa o bloco except
except IOError:
    print('Não foi possível abrir o arquivo\n')
#se não tiver erro, executa else
else:
    print('Arquivo criado com sucesso\n')
    #fechando o arquivo aberto
    f.close()

#utilizando try except e else
try:
    #abrindo arquivo para leitura (vai dar erro afinal esse arquivo não existe)
    f = open('testandoerros', 'r')
#quando ocorrer erro, executa esse bloco
except IOError:
    print('Não foi possível abrir o arquivo\n')
#se o arquivo for aberto com sucesso, executa esse bloco (não vai acontecer)
else:
    print('Leitura feita com sucesso!\n')
    f.close()
    
#usando a função finally
try:
    f = open('testandoerros.txt', 'w')
    f.write('Gravando no arquivo\n')
except IOError:
    print('Não foi possível abrir o arquivo\n')
else:
    print('Arquivo gravado com sucesso!\n')
    f.close()
finally:
    print('Comandos no bloco finally são sempre executados!\n')

'''def AskInt():
    try:
        val = int(input('Digite um número inteiro: '))
    except UnboundLocalError:
        print('Você não digitou um número inteiro!\n')
    finally:
        print('Obrigado!')
    print(val)
    print('')
AskInt()
'''
'''def AskInt():
    try:
        val = int(input('Digite um número inteiro: '))
    except:
        print('Você não digitou um número inteiro!\n')
        val = int(input('Tente novamente. Digite um número inteiro:'))
    finally:
        print('Obrigado!')
    print(val)
    print('')
AskInt()'''

def AskInt():
    while True:
        try:
            val = int(input('Digite um número inteiro: '))
        except:
            print('Você não digitou um número!\n')
            continue
        else:
            print('Obrigada por digitar um número!\n')
            break
        finally:
            print('Fim da execução!\n')
            print('--------------------------------\n\n')	
        print(val)
AskInt()

tuple = (1, 2, 3, 4, 5)
try:
    tuple.append(6)
    for each in tuple:
        print(each)
except AttributeError as e: 
    print('Erro: ', e)
except IOError as e:
    print('Erro: ', e)

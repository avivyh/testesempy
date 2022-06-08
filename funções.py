#  Created by avivyh on 06/06/22.
#  Copyright © 2022  avivyh. All rights reserved.

"""
As funções são um dos principais recursos quando construimos quantidades cada vez maiores de código
para resolver problemas.

Função é um dispositivo que agrupa um conjunto de instruções para que elas possam ser executadas mais
de uma vez. Funções também permitem especificar os parametros que podem servir como entrada parea as funções.

A construção de funções nos permite reutilizar código sem ter que escrevê-lo novamente. 
Com funções, escrevemos o código uma única vez e repetimos a mesma instrução, fazendo a chamada 
da função quantas vezes forem necessárias.

o formato geral de uma função é 
def nome da função(arg1, arg2):
    #comentários da função, documentação da função
    <código>
    <retorno da função>

"""
#criando funções em python
def PrimeiraFunção():
    print('Hello World!')
    print('')

#chamando função
PrimeiraFunção()

#substituindo código da função
def PrimeiraFunção(nome):
    print('Hello',(nome))
    print('')

#Solicitando parametro parea o usuário
Aluno = input('Digite seu nome:\n')
#chamando função
PrimeiraFunção(Aluno)
#chamando função passando parametro manualmente
PrimeiraFunção('Vitória')

#função com for
def FunçãoLeitura():
    for i in range(0, 5):
        print('Número ' + str(i))
FunçãoLeitura()
print('')

#função para somar números
def SomarNúmeros(firstnum, secondnum):
    print('Primeiro número:' + str(firstnum))
    print('Segundo número:' + str(secondnum))
    print('Soma:', firstnum + secondnum)

#chamando função e passando parmetros
SomarNúmeros(1, 2)
print('')

def FunçãoAté10():
    for i in range(0, 11):
        print(i)

FunçãoAté10()
print('')
def TesteFunção():
    for i in range(10, 21):
        print(i)
TesteFunção()
print('')


"""
Váriaveis de dentro de funções são variaveis LOCAIS

estudar python para não criar funções que já existem

"""

#converter entrada de dados para o tipo inteiro
idade = int(input('Digite sua idade:'))
if idade > 13:
    print('Você pode usar o facebook!')
print('')

#convertendo string para valor inteiro
print(int('26'))

#convertendo string para valor float
print(float('23.44'))

#convertendo int para string
print(str(27))
print('')

#função para verificar o comprimento de um objeto
lista = [21, 22, 23, 34, 35]
print(len(lista))
print('')

array = ['a', 'b', 'c']
#varificando o valor maximo do array
print(max(array))
#verificando valor minimo do array
print(min(array))
print('')

#função sum para somar o conteúdo da lista
print(sum(lista))
print('')

#importando o pacote de matematica
#pacote é um conjunto de funções similares, por exemplo, o pacote math possui varias funções matematicas
import math
def NumPrimo(num):
    '''Verificando se um número é primo'''
    if (num % 2 == 0) and (num > 2):
        return 'Este número não é primo.'
    for i in range(3, int(math.sqrt(num))+ 1, 2):
        if(num % i == 0):
            return 'Este número não é primo.'
    return 'Este número é primo.'
print(NumPrimo(542))

#criando função para fazer fatiamento 
def SplitString(texto):
    return texto.split(' ')
texto = 'Essa função será bastante útil para separar grandes volumes de dados!'
#isso vai dividir o texto em uma lista sempre que encontrar a variavel passada na função
print(SplitString(texto))

#gravando o resultado da função em uma variavel
var = SplitString(texto)
print(var)
print('')

str = 'EU AMO ESTUDAR PYTHON!'
def ConverterString(string):
    #essa função vai converter a string para minuscula
    return string.lower()
var = ConverterString(str)
print(var)
print('')


#criando função com um número variado de argumentos, ou seja, podem variar a quantidades de argumentos
#a cada chamada, o segundo argumento significa que será passado UM CONJUNTO DE PARAMETROS
def PrintVarInfo(arg1, *vartuple):
    #imprimindo primeiro argumento
    print('O parametro passado foi: ', arg1)
    #imprimindo valores do segundo argumento
    for item in vartuple:
        print('O parametro passado foi: ', item)
    return
#chamando apenas um argumento
PrintVarInfo(10)
#chamando vários argumentos
PrintVarInfo('Chocolate', 'Morango', 'Uva')



'''
Expressões lambda nos permitem criar expressões anonimas.
isso significa que podemos fazer rapidamente funções ad-hoc sem a necessidade 
de definir uma função usando a palavra reservada def 

principais diferenças: 
- o corpo do lambda é uma única expressão, não um bloco de instruções
- o corpo do lambda é semelhante a uma instrução de retorno do corpo def
    funções lambda realmente são úteis quando utilizadas em conjunto com as funções
    map(), filter(), reduce()
    expressões lambdas também são  usadas para criar funções simples
    são também chamadas funções in-line ou apenas funções anonimas
    ex:
    lambda x: x**2
    (palavra reservada lambda, o primeiro x representa o parametro de entrada e a expressão 
    após os dois pontos é o retorno da função)

    DIFERENÇAS ENTRE DEF E LAMBDA:
    def -> cria um objeto e atribui um nome a ele
    lambda -> cria um objeto mas o retorna como um resultado em tempo de execução

'''

#definindo função def - 3 linhas de código
def Potencia(num):
    result = num**2
    return result 

print(Potencia(5))
print('')

#definindo função def - 2 linhas de código
def Potencia(num):
    return num**2

print(Potencia(5))
print('')

#definindo função def - 1 linha de código
def Potencia(num): return num**2

print('next')


#definindo expressão lambda
#potencia é a váriavel que recebe
#lambda é a expressão, num é o argumento
#após os dois pontos é a expressão que vai ser retornada da função lambda
potencia = lambda num: num**2
print(potencia(5))
print("")


#foi obtido o mesmo resultado, lambda é uma função anonima, sem nome. Em vez de criar nome p função, pode-se criar
#uma variável
#lembre: operadores de comparação retornam booleanas: true ou false 
Par = lambda num: num % 2 == 0
print(Par(3))
print(Par(4))
print(Par(5))
print('')

#passando variável str para lambdda e retornando o primeiro elemento da string
#nomevariavel, exp lambda e argumento, retorno
first = lambda s: s[0]
#imprimindo na tela o retorno da função, passando uma string
print(first('Python'))
print('')

#revertendo a string
Reverso = lambda s: s[::-1]
print(Reverso('Python'))
print('')

#criando função lambda com mais de um parametro
Soma = lambda x, y: x+y
print(Soma(10, 20))
print('')
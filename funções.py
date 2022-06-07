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
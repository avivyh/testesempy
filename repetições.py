#  Created by avivyh on 02/06/22.
#  Copyright © 2022  avivyh. All rights reserved.


#estruturas de repetição em py
#para cada item, em uma série de intens, execute esse bloco de instruções

"""
 for item in seriedeitens:
    Execute essas instruções
"""

"""
Podemos usar o for para objetos sequenciais 
como por ex,
strings, listas, tuplas, elementos de dicionarios, arquivos


Condicionais são usadas sempre que vc quiser executar um comando ou um confunto de comandos 
um número determinado de vezes

"""

#criando uma tupla e imprimindo cada um dos valores
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in tp:
    print(i)

#criando uma lista e imprimindo
Lista = ['Açucar', 'Farinha', 'Ovos', 'Leite']
for i in Lista:
    print(i)


#imprimindo valores no intervalo entre -1 e 20
for i in range(-1, 20):
    print(i)

#unindo repetição com condição
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for cont in lista:
    if(cont % 2 == 0):
        print(cont)


#imprimindo valores no intervalo entre 0 e 500 saltando de 100 3m 100
for i in range(0, 500, 100):
    print(i)

#imprimindo caracter por caracter de uma frase
for i in 'PYTHON É MUITO BOM!!!!!!':
    print(i)
print("")

#loops aninhados 
for i in range(0, 5):
    for a in range(0, 5):
        print(a)
    print('')

#usando operações em uma lista dentro de um for
Lista = [12, 12, 14, 15, 16, 17, 18, 19]
soma = 0
for i in Lista:
    double = i * 2
    soma += double
    print(soma)
print('')

#percorrendo lista de lista
Lista = [[1, 2, 3, 4], [6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16]]
for valor in Lista:
    print(valor)
print('')

#contando a quantidade de itens de uma lista
Lista = [12, 12, 14, 15, 16, 17, 18, 19]
cont = 0
for i in Lista:
    cont+= 1
print(cont)
print("")


#contando o número de colunas
Lista = [[1, 2, 3, 4], [6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16]]
cont = 0
primeiraL = Lista[0]
for i in primeiraL:
    cont += 1
print(cont)
print("\n")


#pesquisando em listas
Lista = [12, 12, 14, 15, 16, 17, 18, 19]
for i in Lista:
    if (i == 18):
        print('Valor encontrado na lista!\n')


#mostrando as chaves de um dicionario
dic = {'k1':'Python', 'k2':'C', 'k3':'C++'}
for i in dic:
    print(i)
print('\n')

#printando a chave e o valor de um dicionário
for c,v in dic.items():
    print(c, v)
print('\n')


'''
While em py

while(exp1):
    print('comando contiua sendo executado enquanto a exp1 for verdadeira')

'''


#  Created by avivyh on 31/05/22.
#  Copyright © 2022  avivyh. All rights reserved.

# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

#criando lista e adicionando elemento por elemento
lista = [1]
lista.append(2)
print(lista)
lista.append(3)
print(lista)
lista.append(4)
print(lista)
lista.append(5)
print(lista)
lista.append(6)
print(lista)
lista.append(7)
print(lista)
lista.append(8)
print(lista)
lista.append(9)
print(lista)
lista.append(10)
print(lista)
#criando lista e adicionando todos os elementos de uma só vez
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
print('')



# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
#criando lista de string
lista = ['Lápis', 'Mouse', 'Cadeira', 'Mesa', 'Agenda']
print(lista)
print('')



# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
#concatenando duas strings em uma terceira string
name1 = 'PY'
name2 = 'THON'
NomeCompleto = name1 + name2
print(NomeCompleto)
print('')



# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
#usando a função count para verificar quantas vezes o número 4 aparece
tup = (1, 2, 2, 3, 4, 4, 4, 5)
print(tup.count(4))
print('')


# Exercício 5 - Crie um dicionário vazio e imprima na tela
#criando dicionário vazio
dicionario = {}
print(dicionario)
print('')


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
#criando dicionario com chaves e valores
dic = {'chave1':1, 'chave2':2, 'chave3':3}
print(dic)
print('')


# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
#adicionando nova chave e valor ao dicionário
dic['chave4'] = 4
print(dic)
print('')



# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
#criando uma lista aninhada
di = {'one':1, 'two':[2.1, 3.1], 'tree': 3}
print(di)
print('')


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.

lista = ['string', (2, 3), {2:3, 4:5}, 6.7]
print(lista)
print('')

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 0 a 18.
txt = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(txt[0:18])
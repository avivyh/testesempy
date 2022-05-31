#  Created by avivyh on 31/05/22.
#  Copyright © 2022  avivyh. All rights reserved.

"""
    Em python, tuplas são muito semelhantes a listas. A principal diferença é
    que tuplas são imutáveis, ou seja, não podem ser alteradas.

    tuplas são construidas com o uso de parenteses e virgula.
    ex: 
    tupla = (item1, item2, item3)
    ps: listas são criadas com colchetes, dicionários são criados com chaves e tuplas são criadas com parenteses.

"""

#criando uma tupla

tupla = ("Geografia", 23, "Elefantes")
print(tupla)
print('')

# a tupla é imutável, logo as operações de alteração, como
#           tupla.append("Chocolate")
# ou exclui a tupla inteura, ou não exclui.
#           del tupla['Geografia']
#não vão executar

#tuplas podem ter um único item
tupla1 = ('Chocolate')
print(tupla1)
print('')

tupla1 = ("Geografia", 23, "Elefantes")
#verificando primeiro valor armazenado em uma tupla
print(tupla[0])
print('')

#verificando comprimento de uma tupla
print(len(tupla1))
print('')

#fazendo fatiamento, retornando todos os elementos a partir de uma posição
print(tupla1[1:])
print('')

#verificando qual o indice de um dos elementos da tupla
print(tupla1.index('Elefantes'))
print('')

#não é possivel fazer atribuição de um único item da tupla
# ex:
#     tupla1[1] = 1
# vai ter mensagem de erro.

#é possivel deletar a tupla com todos os dados
del tupla1
del tupla

#criando nova tupla
tup = ('A', 'B', 'C')
print(tup)
print('')

"""

    para poder alterar o valor de uma tupla, é necessário converter a tupla para uma lista, só assim será possível 
    fazer modificações.

"""
#usando a função list para converter uma tupla para lista
lis = list(tup)
print(lis)
print('')

#adicionando elemento na lista
lis.append('D')

#usando a função tuple para converter uma lista para tupla

tup = tuple(lis)
print(tup)
print('')
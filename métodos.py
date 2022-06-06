#  Created by avivyh on 06/06/22.
#  Copyright © 2022  avivyh. All rights reserved.

"""
Métodos são funções incorporadas em objetos

ex:
objeto.método(arg1, arg2, etc)

"""

#criando uma lista
from re import A


lista = [1, 2, 3, 0, -50]

#usando um método do objeto lista
#método para adicionar elemento em uma lista
lista.append(10)
print(lista)
print("")

#para saber quantas vezes aparece um elemento especifico na lista
print(lista.count(10))
print('')


#a função help explica como utilizar cada método de um onjeto
help(lista.count) 
print('\n\n')

#a função dir mostra todos os métodos e atributos que estão disponíveis para um objeto
print(dir(lista))
print('')


a = 'Uma String'
# o método de um objeto pode ser chamado dentro de uma função, como print()
# o método split serve para dividir uma string toda vez que encontrar um caracter especifico
# o caracter automatico quando não é passado nenhum outro, é o caracter de espaço
print(a.split())
print('')
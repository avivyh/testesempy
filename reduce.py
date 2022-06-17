'''
REDUCE É UMA FUNÇÃO QUE RECEBE DOIS ARGUMENTOS
- uma função
- uma sequência

o primeiro argumento é o nome de uma função e o segundo é uma sequência, 
como por exemplo, uma lista.

AO CONTRÁRIO DA FUNÇÃO MAP QUE APLICA UMA FUNÇÃO A CADA UM DOS ITENS DE UMA SEQUÊNCIA,
A FUNÇÃO REDUCE APLICA A FUNÇÃO QUE FOI RECEBIDA COMO PARAMETRO AOS ELEMENTOS DA SEQUÊNCIA 
ATÉ QUE RESTE APENAS UM ELEMENTO.

'''
#importando o método reduce do módulo functools
from functools import reduce
from re import X

#criando lista
lista = [47, 11, 42, 13]
print(lista)

#função para somar
def soma(a, b):
    x = a + b
    return x

#usando reduce com uma função e uma lista. a função vai
#retornar a soma de todos os valores.
#passando como argumento a função soma e a sequencia lista
print(reduce(soma, lista))
print('')

#usando a função reduce() com lambda
print(reduce(lambda x, y: x+y, lista))
print('')

#podemos atribuir a expressão lambda a uma variável, que vai ser do tipo função
#a função lambda recebe a e b como parametros, verifica 
#se a é maior que b, se sim, retorna a, se não, retorna b.
find = lambda a, b: a if (a>b) else b

#usando a função find crianda com lambda com o reduce
print(reduce(find, lista))
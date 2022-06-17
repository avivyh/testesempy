'''

LIST COMPREHENSION APLICA UMA EXPRESSÃO ARBITRÁRIA (AO INVES DE APLICAR 
APENAS UMA FUNÇÃO) A UMA SEQUÊNCIA DE ELEMENTOS.

LIST COMPREHENSION PERMITE DESENVOLVER LISTAS USANDO UMA NOTAÇÃO DIFERENTE.
É ESSENCIALMENTE UMA LINHA DE LOOP FOR, CONSTRUIDA DENTRO DE [].

EX:
    lista=[x for x in "sequencia"]

geralmente usamos loops for quando trabalhamos com funções map
e usamos list comprehension quando esta for mais facil de ser aplicada

no entanto, há uma vantagem substancial de desempenho ao utilizar a list comprehension
o desempenho é melhor.

'''

#retorna cada caracter em um conjunto de caracteres
lista = [x for x in 'python']
print(lista)

#LISTA RECEBE A RAIZ QUADRADA DE UM RANGE DE NÚMEROS
#lista recebe uma lista que recebe os comandos para 
#cada elemento da lista
lista = [x**2 for x in range(0,11)]
print(lista)
print("")

#para cada x na lista de 0 a 10, se x for par, o objeto lista recebe x
lista = [x for x in range(11) if x % 2 == 0]
print(lista)
print('')
#convertendo celsius para fahrenheit
#criando lista
celsius = [0, 10, 20.1, 34.5]

#criando uma nova lista realizando um calculo em cada elemento da lista
#celsius

#retornando o resultado do calculo para cada elemento temp na lista celsius
fahrenheit = [((float (9)/5)* temp + 32) for temp in celsius]
print(fahrenheit)
print('')

#criando um list comprehension aninhado
#primeiro, é executada a lista interna do range
#depois é executada a lista externa
lista = [x**2 for x in [x**2 for x in range(11)]]
print(lista)
print('')
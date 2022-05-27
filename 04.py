#Listas em python
"""
Listas são consideradas a visão geral de
uma sequencia em python. As listas são mutáveis, ou seja, 
os elementos de uma lista podem ser alterados.

Listas não tem tamanho fixo
Listas não tem restricões de tipo fixo

Uma caracteristica de estruturas de dados em python é que elas
suportam aninhamento, ou seja, podemos usar estruturas de dados
dentro de estruturas de dados

lista = [item1, item2]

"""
#criando uma lista
#Nesse caso, temos três elementos na lista
ListaMercado = ['Ovos', 'Farinha', 'Leite']
print(ListaMercado)

#Nesse caso, temos somente um elemento na lista
ListaMercado2 = ['Chocolate, Biscoito, Suco']
print(ListaMercado2)

print('')
print(ListaMercado[0])
print(ListaMercado2[0])
print('')

#Logo, o correto, será utilizar aspas e virgulas para separar os elementos
ListaMercado2 = ['Chocolate', 'Biscoito', 'Suco']
print(ListaMercado2)
print('')
print(ListaMercado[0])
print(ListaMercado2[0])
print('')

#criando lista com elementos de diferentes tipos
Lista = [1, 4.5, 'Algoritmos']
print(Lista)
print('')
print(Lista[0])
print(Lista[1])
print(Lista[2])
print('')
#passando valores p variaveis
item1 = Lista[0]
item2 = Lista[1]
item3 = Lista[2]
print(item1, item2, item3)
print('')

#Alterar valor da lista
print(ListaMercado[0])
ListaMercado[0] = 'Chocolate'
print(ListaMercado)
print('')

#deletando item da lista 
#só é possível deletar itens que existem!!!!
del ListaMercado[2]
print(ListaMercado)
print('')

#Criando listas de listas ou lista aninhada 
#cada elemento é formado por uma lista
lista = [[1, 2, 3], [11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(lista)
print("Imprimindo o primeiro elemento de uma lista aninhada:", lista[0])

#passando o primeiro elemento da lista aninhada para uma variavel
a = lista [0]
#imprimindo a variavel que recebeu um elemento da lista
print(a)
#observe que é possível fatiar os valores que existem no elemento
print(a[0])
print(a[1])
print(a[2])
print('')

#trabalhando com lista aninhada 
print(lista[1][0])

#IMPRIMINDO A LISTA ANINHADA COMPLETA
i = 0 
while i<3:
    print(lista[i][0], lista[i][1], lista[i][2])
    i+=1
print('')


#concatenando duas listas
NewLista = lista  + ListaMercado
print(NewLista)


#verificando se existe um elemento dentro de uma lista 
print(11 in lista)
print([1, 2, 3] in lista)

print('')
print(1 in Lista)

#verificando o comprimento de uma lista
print(len(lista))
print('')

#retornando o maior valor de uma lista 
print(max(lista))

#retornando o menor valor de uma lista 
print(min(lista))
print('')

#Adicionando elemento no final da lista 
ListaMercado2.append('Açucar')
print(ListaMercado2)
#a mesma string pode ser adicionada mais de uma vez, se isso não puder ocorrer
#será necessária uma estrutura condicional para impedir
ListaMercado2.append('Açucar')
print(ListaMercado2)
print('')
#checando quantas vezes um elemento aparece na lista
print(ListaMercado2.count('Açucar'))
print('')
#criando lista vazia
a = []
print(a)
print(type(a))
print('')

#adicionando elementos em a
a.append(10)
print(a)
a.append(20)
print(a)
a.append(30)
print(a)
print('')

#criando listas
ListaAntiga = [70, 80, 90, 100]
ListaAtual = []

#preenchendo a lista atual com elementos da lista antiga
for item in ListaAntiga:
    ListaAtual.append(item)
print(ListaAtual)
print('')

#criando lista e adicionando itens
c = [20, 25]
print(c)
c.append(30)
c.append(35)
print(c)

#criando listas de strings 
print('')
Cidades = ['Recife', 'Salvador', 'Rio de Janeiro', 'Teresina']
Cidades.extend(['Palmas', 'Fortaleza'])
print(Cidades)

#buscando indice de um elemento em uma lista 
#nem sempre isso vai funcionar
print(Cidades.index('Fortaleza'))
print('')

#inserindo um elemento na lista especificando em qual posição esse elemento vai ser armazenado
Cidades.insert(2, 'Picos')
print(Cidades)

#eliminando elemento especifico na lista
Cidades.remove('Picos')
print(Cidades)
print('')

#revertendo elementos da lista
Cidades.reverse()
print(Cidades)

#criando lista 
x = [100, 99, 98, 7, 95, 94, 93]
#ordenando elementos da lista
x.sort()
print(x)
print('')
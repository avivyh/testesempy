'''

A LINGUAGEM PYTHON FORNECE VÁRIAS FUNÇÕES QUE PERMITEM UMA ABORDAGEM FUNCIONAL
À PROGRAMAÇÃO, OFERECENDO MAIS FACILIDADE NA CRIAÇÃO DO SEU CÓDIGO.

PODEMOS DIZER QUE A PROGRAMAÇÃO FUNCIONAL É UMA PROGRAMAÇÃO ORIENTADA
A EXPRESSÃO.

exemplos de funções orientadas a expressão:	
    map(função, sequencia)
    reduce(função, sequencia)
    filter(função, sequencia)
    lambda
    list comprehension
    
uma coisa comum comlistas e outras funções em python é 
aplicar uma operação para cada um dos itens de uma sequencia, e receber um
resultado.
ex :
lista = [1, 2, 3, 4, 5]
quadrados = []
    for i in lista:
        quadrados.append(i**2)
quadrados terá como resultado [1, 2, 9, 16, 25]



MAP É UMA FUNÇÃO QUE RECEBE DOIS ARGUMENTOS: UMA FUNÇÃO E UMA SEQUENCIA
ELA APLICA A FUNÇÃO QUE ELA RECEBEU EM UM PARAMETRO A CADA UM
DOS ITENS EM UM OBJETO QUE SEJA INTERÁVEL

O primeiro argumento é o nome de uma função e o segundo
é uma sequencia(por ex, uma lista)
    map(função, sequencia)
    
a função map aplica a função que foi recebida como parametro
a todos os elementos da sequencia, e uma nova lista com os elementos
alterados pela função é retornado

'''

#criação de duas funções
#função 1 - recebe uma temperatura como parametro e retorna a temp
#em fahrenheit
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

#função 2 - recebe uma temperatura como parametro e retorna a temp
#em celsius
def celsius(T):
    return(float(5)/9*(T - 32))

#criando uma lista 
temperaturas = [0, 22.5, 40, 100]

#aplicando a função a cada elemento da lista
#em python, a função map retorna um objeto iterável, então precisamos converter para uma lista
#a função map vai aplicar a função fahrenheit a cada elemento
#da lista temperaturas e vai retornar uma nova lista com os resultados
new = list(map(fahrenheit, temperaturas))
print(new)
print("")


#imprimindo elemento por elemento
for temp in map(fahrenheit, temperaturas):
    print(temp)
print('')

#convertendo o resultado de map p uma lista
new = list(map(celsius, temperaturas))
print(new)
print("")

#usando a função lambda
new = list(map(lambda x: (5.0/9)*(x-32), temperaturas))
print(new)

#somando os elementos de duas listas
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
#passando a soma desses elementos para uma nova lista
#converte pro tipo lista, chama a map, passa a
#função lambda como primeiro argumento e a sequencia como segundo argumento
new = list(map(lambda x, y: x+y, a, b))
print(new)
print('')

c = [9, 10, 11, 12]
#converte o retorno p lista new
#chama a função map que recebe como primeiro arg a função lambda
#a função lambda tem três argumentos e retorna a soma dos três
#o segundo argumento da função map são três listas
new = list(map(lambda x, y, z: x+y+z, a, b, c))
print(new)
print('')
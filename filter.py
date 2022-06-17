'''A EXEMPLO DAS FUNÇÕES BUILT-IN, MAP() E REDUCE(), A FUNÇÃO
FILTER() TAMBÉM RECEBE DOIS ARGUMENTOS, UMA FUNÇÃO E UMA SEQUÊNCIA.
EX:
    filter(função, sequência)
a função retorna true ou falso

A FUNÇÃO SERÁ APLICADA A TODOS OS VALORES DE UMA SEQUÊNCIA E OS VALORES
SERÃO RETORNADOS, APENAS SE RETORNAREM TRUE PARA A FUNÇÃO.

'''
#CRIANDO UMA FUNÇÃO
def verificaPar(num):
    if (num % 2 == 0):
        return True
    else:
        return False

#chamando a função e passando um número como parametro
#retornará falso se for impar e true se for par.
print(verificaPar(35))
print('')
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
print(lista)
print('')

#convertendo os valores que retornarem true na função verificaPar() para 
#uma lista
print(list(filter(verificaPar, lista)))
print("")

#usando filter com a função lambda
#converte o resultado p uma lista
# a função filter recebe como primeiro parametro a função lambda
# que varifica se um numero é par ou não
# e como segundo parametro recebe a sequencia lista
#a função lambda recebe um unico argumento e retorna se 
#esse numero é par ou não
print(list(filter(lambda x: x % 2 == 0, lista)))
print('')

#usando filter com a função lambda
#converte o resultado p uma lista
# a função filter recebe como primeiro parametro a função lambda
# que varifica se um numero é maior que 8
# e como segundo parametro recebe a sequencia lista
#a função lambda recebe um unico argumento e retorna se 
#esse numero for maior que 8
print(list(filter(lambda x: x > 8, lista)))
print('')
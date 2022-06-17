# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
lista = 3, 4, 5
#criei uma lista e em seguida, criei uma lista comprehension para elevar a potencia 3 de todos os
#elementos da primeira lista
lst = [x**3 for x in lista]
print(lst)

# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
'''palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)'''

palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
#a váriavel i recebe uma lista com o resultado da função map, que vai pegar cada elemento da variavel
#palavras e chamar a função lambda como primeiro argumento e a sequencia como segundo argumento
i = list(map(lambda x: [x.upper(), x.lower(), len(x)], palavras))
print(i)


# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]
lst = list(map(lambda x: x**2, lista)), list(map(lambda x: x**3, lista))
print(lst)
print("")

# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]
lst = list(map(lambda x, y: x**y, listaA, listaB))
print('')

# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
range(-5, 5)
def VerificaNegativo(x):
    if(x < 0):
        return True
    else:
        return False
print(list(filter(VerificaNegativo, range(-5, 5))))
print('')

# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(list(filter(lambda x: x in a, b)))

# Exercício 9 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}
dict3 = {}

def Func(d1, d2):
    for k, v in zip(d1, d2.values()):
        dict3[k] = v
    return dict3
print(Func(dict1, dict2))
print('')

# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
list = list(filter(lambda x: x > '5', lista))
print(list)
#ps: não da p comparar string e número, apenas string e string.
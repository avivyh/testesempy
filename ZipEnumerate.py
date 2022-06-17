'''

A FUNÇÃO ZIP AGREGA OS VALORES DE DUAS SEQUENCIAS E RETORNA UMA TUPLA
EX:
    zip(sequência, sequência)
    
ZIP PODE SER USADO QUANDO O NÚMERO DE ELEMENTOS FOR DIFERENTE EM CADA SEQUENCIA
MAS O OBJETO RESULTANTE TERÁ O MESMO NÚMERO DE ELEMENTOS DA SEQUENCIA
MENOR.

EX:
    zip([1, 2, 3, 4], [1, 2, 3])
    (1, 1) (2, 2) (3, 3)
    
a função zip sempre vai considerar o tamanho da lista que tem o menor
número de elementos.


OUTRA FUNÇÃO BASTANTE ÚTIL É ENUMERATE
A FUNÇÃO ENUMERATE PERMITE RETORNAR O ÍNDICE DE CADA VALOR EM UMA
SEQUENCIA, À MEDIDA QUE VOCÊ PERCORRE TODA A SEQUÊNCIA.

ENUMERATE RETORNA UMA TUPLA NO FORMATO tupla(índice, valor)

'''

#criando listas
x = [1, 2, 3]
y = [4, 5, 6]

#unindo as listas, em python3 retorna um interator
zip(x, y)
#então precisamos converter para uma lista, neste caso, uma lista de tuplas
print(list(zip(x, y)))
print('')

#ATENÇÃO QUANDO AS SEQUÊNCIAS TIVEREM YM NÚMERO DIFERENTE DE VALORES
print(list(zip('ABC', 'xy')))
print('')

#criando listas 
a = [1, 2, 3]
b = [4, 5, 6, 7, 8]

#imprimindo o resultado convertido pro tipo lista 
print(list(zip(a, b)))
print('')

#criando dois dicionários
d1 = {'a': 1, 'b': 2}
d2 = {'c': 4, 'd': 5}

#zip vai unir as chaves
print(list(zip(d1, d2)))

#zip pode unir os valores
print(list(zip(d1.values(), d2.values())))
print('')

#zip pode utilizar uma chave e um valor, ou vice versa
print(list(zip(d1, d2.values())))
print('')

#criando função para trocar valores entre os dois dicionários
def trocaValores(d1, d2):
    dicTemp =  {}
    #para cada chave no primeiro dicionário, e cada valor no segundo 
    #dicionário
    for d1key, d2val in zip(d1, d2.values()):
        #o novo dicionário vai receber a chave do primeiro dicionário
        # e o valor armazenado no segundo dicionário
        dicTemp[d1key] = d2val
        #no fim, retornamos o dicionário temporário
    return dicTemp
print(trocaValores(d1, d2))
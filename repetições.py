#  Created by avivyh on 02/06/22.
#  Copyright © 2022  avivyh. All rights reserved.


#estruturas de repetição em py
#para cada item, em uma série de intens, execute esse bloco de instruções

"""
 for item in seriedeitens:
    Execute essas instruções
"""

"""
Podemos usar o for para objetos sequenciais 
como por ex,
strings, listas, tuplas, elementos de dicionarios, arquivos


Condicionais são usadas sempre que vc quiser executar um comando ou um confunto de comandos 
um número determinado de vezes

"""

#criando uma tupla e imprimindo cada um dos valores
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in tp:
    print(i)

#criando uma lista e imprimindo
Lista = ['Açucar', 'Farinha', 'Ovos', 'Leite']
for i in Lista:
    print(i)


#imprimindo valores no intervalo entre -1 e 20
for i in range(-1, 20):
    print(i)

#unindo repetição com condição
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for cont in lista:
    if(cont % 2 == 0):
        print(cont)


#imprimindo valores no intervalo entre 0 e 500 saltando de 100 3m 100
for i in range(0, 500, 100):
    print(i)

#imprimindo caracter por caracter de uma frase
for i in 'PYTHON É MUITO BOM!!!!!!':
    print(i)
print("")

#loops aninhados 
for i in range(0, 5):
    for a in range(0, 5):
        print(a)
    print('')

#usando operações em uma lista dentro de um for
Lista = [12, 12, 14, 15, 16, 17, 18, 19]
soma = 0
for i in Lista:
    double = i * 2
    soma += double
    print(soma)
print('')

#percorrendo lista de lista
Lista = [[1, 2, 3, 4], [6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16]]
for valor in Lista:
    print(valor)
print('')

#contando a quantidade de itens de uma lista
Lista = [12, 12, 14, 15, 16, 17, 18, 19]
cont = 0
for i in Lista:
    cont+= 1
print(cont)
print("")


#contando o número de colunas
Lista = [[1, 2, 3, 4], [6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16]]
cont = 0
primeiraL = Lista[0]
for i in primeiraL:
    cont += 1
print(cont)
print("\n")


#pesquisando em listas
Lista = [12, 12, 14, 15, 16, 17, 18, 19]
for i in Lista:
    if (i == 18):
        print('Valor encontrado na lista!\n')


#mostrando as chaves de um dicionario
dic = {'k1':'Python', 'k2':'C', 'k3':'C++'}
for i in dic:
    print(i)
print('\n')

#printando a chave e o valor de um dicionário
for c,v in dic.items():
    print(c, v)
print('\n')


'''
While em py

while(exp1):
    print('comando contiua sendo executado enquanto a exp1 for verdadeira')

'''

#usando while para imprimir de 0 a 9
cont = 0
while ( cont < 10):
    print(cont)
    cont+=1
print("\n")


# é possível usar else com while em python
x = 0
while x<10:
    print('A váriavel está no loop\n')
    x+=1
else:
    print('Loop encerrado!\n')


#pass, break e continue
cont = 0
while (cont<100):
    if (cont == 4):
        #break interrompe o while
        break
    else:
        pass
        #continua seguindo a execução dentro do while
    print(cont)
    cont += 1
print('\n')

for i in 'python':
    if (i == 'h'):
        #usado para pular uma iteração
        continue
    print(i)
print('')


#while e for juntos
#imprimindo numeros primos no intervalo de 2 a 50
for i in range(2, 50):
    j = 2
    cont = 0
    while j<i:
        if i % j == 0:
            cont = 1
            j = j + 1
        else:
            j = j + 1
    if cont == 0:
        print(str(i) + ' é um número primo')
        cont = 0
    else:
        cont = 0
print("")


"""
Função Range

essa função nos permite criar uma lista de números em um intervalo especifíco
range([start], [stop], [step]) - 
start - número que inicia a sequencia
stop - número que encerra a sequencia (não é inserido na sequencia)
step - diferença entre cada número da sequencia

"""

#imprimindo números pares entre 50 e 100
for i in range(50, 101, 2):
    print(i)
print('')

#se não tiver o terceiro elemento, o padrão será 1 em 1
for i in range(3, 6):
    print(i)
print('')

#também é possível saltar p trás
for i in range(0, -20, -2):
    print(i)
print('')


#usando for quando vc tem uma sequencia e não sabe o tamanho fixo
lista = ['banana', 'morango', 'abacaxi', 'uva']
ListaTamanho = len(lista)
for i in range(0, ListaTamanho):
    print(lista[i])
print('')



#imprimindo todas as strings menos uma
nome = 'Luan Santana'
for i in nome:
    if( i == ' '):
        continue
    print(i)
print('')



#imprimindo numeros impares
for i in range(0, 101):
    if(i % 2 != 0):
        print(i)
print('')
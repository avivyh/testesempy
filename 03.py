#  Created by avivyh on 27/05/22.
#  Copyright © 2022  avivyh. All rights reserved.


#strings
#indexação em py começa com 0
#Python utiliza aspas siples ou duplas para strings
#strings em python são imutáveis
print("Testando strings em python")
#quebra de linha \n
print("\n")
print('Testando\nStrings\nEm\nPython\n')

#criando string e imprimindo 
s = "Eu adoro estudar python"
print(s)

#pegando a primeira posição da string pelo indice 0
print(s[0])

#slicing (fatiamento)
#retornando todos os elementos de uma posição, começando pela posição x, até o fim da string
print(s[3:])

#a string original não é alterada
print("string original:",s)

#retorna tuydo até a posição 3
print(s[:5])

#Retornando tudo em s
print(s[:])

#usando indexação ao contrario
#vai ser pego a ultima letra
print('Ultima letra:',s[-1])

#retornar tudo menos a ultima letra:
print(s[:-1])

#podemos utilizar a notação de indice e fazer a fatiação em pedaços específicos
print("um em um: ",s[::1])
print("dois em dois: ", s[::2])

#printando a string de trás pra frente
print("String contraria:", s[::-1])
print("String contraria de dois em dois:", s[::-2])

#concatenação de string
s += ' é muito produtivo!'
print(s)

#multiplicando string
letra = 'X'
print(letra * 3)

print('\n')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Funções Built-in de strings
#transformando string em capitular (maiúsculo)
print(s.upper())
print('\n')

#transformando string em minusculo
print(s.lower())
print('\n')

#dividindo a string 
#sem parâmetros, faz a divisão por espaço em branco
print(s.split())
#com parametro faz a divisão cada vez que encontra a string passada por parâmetro
print(s.split('o'))
print('\n')


#FUNÇÔES STRING
s = 'barbie em vida de sereia!'
#transformando a primeira letra em maiuscula
print(s.capitalize())

#contando quantas vezes um caracter aparece
print(s.count('a'))

#encontrar a posição de um caracter na string
print(s.find('v'))

#verificando se tem caracter minusculo na string 
print(s.islower())

#verificando se a string tem apenas espaço
print(s.isspace())

#verificando se a string termina com a letra b
print(s.endswith('b'))
print('\n')
#comparando strings
print('python' == 'R')
print('python' == 'python')
#  Created by avivyh on 08/06/22.
#  Copyright © 2022  avivyh. All rights reserved.

from platform import python_version
# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20
# (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números      
def Pares():
    #criando função sem parametro para imprimir números pares entre 1 e 20
    for i in range(1, 20):
        if(i % 2 == 0):
            print(i)
#chamando a função para listar os números
Pares()
print("")

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne 
# a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
def Maiusculas(str):
    #retornando a string recebida utilizando a função upper, para 
    #converter as letras para maiusculas
    return str.upper()
string = 'python é a lingua dos deuses!'
#imprimindo função e passando string
print(Maiusculas(string))
print('')

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos,
#  adicione 2 elementos a lista e imprima a lista
def FunçãoImprimeLista(lista):
    lista.append('Uva')
    lista.append('Abacaxi')
    print(lista)
lista = ['Morango', 'Banana', 'Maça', 'Pera']
FunçãoImprimeLista(lista)
print('')

# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. 
# Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
def FunçãoElementos(arg1, *agr2):
    print('o argumento foi:', arg1)
    for i in agr2:
        print('o argumento foi:', i)
FunçãoElementos(10)
print('')
FunçãoElementos(10, 20, 30, 40)
print('')

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma.
#  A expressão vai receber 2 
# números como parâmetro e retornar a soma deles
soma = lambda x, y: x+y
print(soma(10, 30))
print('')


# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre 
# variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total

soma( 10, 20 )
print ("Fora da função o total é: ", total)
print('')
#isso acontece porque variáveis locais só existem dentro da função, logo dentro da função o valor
#da variável local é alterado


# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda num: (float(9)/5)* num + 32, Celsius)
print (list(Fahrenheit))
print('')

# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário
dicionário = {1:'Chave 1', 2:'Chave 2'}
print(dir(dicionário))
print('')

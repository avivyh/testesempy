# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana.
#  Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso",
#  caso contrário imprima na tela "Você precisa trabalhar!"

dia = input('Qual dia da semana?')
if(dia == 'Sábado') or (dia == 'Domingo'):
    print('Hoje é dia de descanso!\n')
else:
    print('Você precisa trabalhar!')
print('')

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
lista = ['Uva', 'Laranja', 'Morango', 'Maça', 'Banana']
for i in lista:
    if(i == 'Morango'):
        print('Existe', i, 'na lista!')
print('')

# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da 
# tupla por 2 e guarde os resultados em uma 
# lista
lista = []
j = 1
tupla = (1, 2, 3, 4)
for i in tupla:
    j = i*2
    lista.append(j)
print(lista)
print("")

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for i in range(100, 151):
    if(i % 2 == 0):
        print(i)
print('')


# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto 
# temperatura for maior que 35, 
# imprima as temperaturas na tela
temperatura = 40
while(temperatura>35):
    print(temperatura)
    temperatura-=1
print("")

# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100,
#  imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
contador = 0
while (contador < 100):
    if(contador == 23):
        break
    print(contador)
    contador+=1
print('')

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da 
# variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista

lista = []
valor = 4
while (valor <=20):
    if(valor % 2 == 0):
        lista.append(valor)
        valor+=1
    else:
        valor+=1
print(lista)
print('')

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
lista = []
print(lista)
for i in range(5, 45, 2):
    lista.append(i)
print(lista)
print('')

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if (temperatura > 30):
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece 
# na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; 
# se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)
cont = 0
frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir." 
for i in frase:
    if(i == 'r') or (i == 'R'):
        cont+=1
print('A letra "r" apareceu %r vezes' %(cont))
print('')
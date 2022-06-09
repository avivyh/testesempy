#  Created by avivyh on 09/06/22.
#  Copyright © 2022  avivyh. All rights reserved.

#solicitando ao usuario o nome do arquivo
FileName = input('Digite o nome do arquivo:')
#concatenando texto
FileName = FileName + '.txt'
#abrindo arquivo para modo escrita
arquivo1 = open(FileName, 'w')
#sobrescrevendo conteudo
arquivo1.write('Incluindo conteudo no arquivo!')
#fechando conexão do arquivo
arquivo1.close()

#abrindo arquivo para o modo leitura
arquivo1 = open(FileName, 'r')
#lendo conteudo do arquivo
print(arquivo1.read())
#fechando arquivo
arquivo1.close()
print('')

#abrindo arquivo para leitura
f = open('teste.txt', 'r')
#passando conteudo para variavel
data = f.read()
#dividindo em uma lista toda vez q encontra uma quebra de linha e passando conteudo p variável
rows = data.split('\n')
#imprimindo lista
print(rows)
print('')

#criando lista vazia
lista = []

#criando repetição para percorrer a primeira lista
for row in rows:
    #dividindo o conteudo em uma variavel
    splitrow = row.split(',')
    #adicionando na lista vazia
    lista.append(splitrow)
print(lista)
#fechando arquivo
f.close()

#contando as linhas de um arquivo
#abrindo arquivo no modo leitura
f = open('salarios.csv', 'r')
#passando conteudo do arquivo para variável
data = f.read()
#passando para a variavel rows o fateamento do arquivo toda vez que é encontrada uma quebra de linha
rows = data.split('\n')
#criando lista vazia
lista = []
for row in rows:
    #passando p variavel todas as vezes que tiver uma quebra de linha
    splitrow = row.split('\n')
    #adicionando na lista
    lista.append(splitrow)
print(lista)
print("")
cont = 0
#percorrendo a lista
for row in lista:
    #incrementando +1 para cada elemento da lista
    cont += 1
#printando a quantidade de quebras de linhas encontradas (no caso, a quantidade de frases)
print(cont)
print("")
#fechando arquivo
f.close()

#abrindo arquivo para leitura
arq = open('salarios.csv', 'r')
#lendo e imprimindo o conteudo do arquivo
print(arq.read())
print('')
#o cursor foi pro fim do arquivo, ou seja, não vai encontrar mais nada p ler no arquivo, se
#tentar ler novamente não vai aparecer nada pois estamos na ultima posição do arquivo!
#para conseguir ler novamente, precisamos apontar para o inicio do arquivo
arq.seek(0, 0)
#lendo o arquivo linha a linha
print(arq.readlines())
print('')
#podemos usar o loop for para percorrer cada linha de um arquivo
#variavel, abrir arquivo, nome do arquivo
for linha in open('salarios.csv'):
    print(linha)
print('')
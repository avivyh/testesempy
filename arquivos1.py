''' 
Arquivos

Métodos 

open()              -> abrir um arquivo
read()              -> leitura de um arquivo
write()             -> gravação em um arquivo
seek()              -> retorna para o ínicio do arquivo
readlines()         -> retorna a lista de linhas do arquivo
close()             -> fecha o arquivo


'''


#abrindo um arquivo para leitura 
arquivo1 = open('arquivo1.txt', 'r')

#lendo o arquivo (que está na váriavel)
print(arquivo1.read())

#contando o número de caracteres
print(arquivo1.tell())

#retornando para um ponto especifico do arquivo (nesse caso, o inicio)
print(arquivo1.seek(0, 0))

#usando read para ler uma quantidade especifica de caracteres
print(arquivo1.read(10))

#abrindo arquivo para escrita
arquivo1 = open('arquivo1.txt', 'w')

#gravando (sobrescrevendo) no arquivo
arquivo1.write('Python eh muito legal!\n')
arquivo1 = open('arquivo1.txt', 'r')
print(arquivo1.read())
#fechando o arquivo
arquivo1.close()
print('')

#acrescentando conteudo em um arquivo e fechando o arquivo
arquivo1 = open('arquivo1.txt', 'a')
arquivo1.write('Acrescentando conteudo\n')
arquivo1.close()

#abrindo arquivo para leitura
arquivo1 = open('arquivo1.txt', 'r')
print(arquivo1.read())

#voltando ao inicio para leitura
arquivo1.seek(0, 0)
#fazendo a leitura
print(arquivo1.read())
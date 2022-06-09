#  Created by avivyh on 09/06/22.
#  Copyright © 2022  avivyh. All rights reserved.


#importando pandas que é um conjunto de um pacote para analise de dados
import pandas as pd
#passando nome do arquivo para variavel filename
fileName = 'binary.csv'
#fazendo a leitura do arquivo para dentro de um objeto
df = pd.read_csv(fileName)
#imprimindo apenas as primeiras linhas (ou seja, a caeça do arquivo)
print(df.head())
print('')

#abrindo arquivo com pandas 
#passando nome do arquivo para variável
file2 = 'salarios.csv'
#fazendo a leitura de um arquivo pra dentro de um objeto
df2 = pd.read_csv(file2)
#printando o arquivo
print(df2.head())
print('')
print('')


'''Manipulação de arquivos'''
#variavel texto recebe frase
texto = 'Cientista de dados eh a profissao que mais tem crescido no mundo.\n'
#concatenando texto
texto = texto + 'Esses profissionais precisam se especializar em programacao, estatistica e machine learning.\n'
#concatenando de novo
texto += 'E claro, em big data.\n'

#imprimindo o resultado
print(texto)
print('')

#importando módulo os
import os 
#criando arquivo 
arquivo = open('cientista.txt', 'w')

#gravando no arquivo
#para cada palavra na variavel texto, fatiando essa variavel por casa espaço encontrado, 
#passaremos o conteudo para o arquivo
for palavra in texto.split():
    #escrevendo no arquivo
    arquivo.write(palavra + ' ')
#fechando o arquivo
arquivo.close()

#lendo o arquivo para leitura
arquivo = open('cientista.txt', 'r')
#lendo o conteudo do arquivo e passando p variavel conteudo
conteudo = arquivo.read()
#fechando o arquivo
arquivo.close()
#imprimindo conteudo
print(conteudo)
print("")


''' Usando a expressão WITH'''
#o metodo close() é executado automaticamente
with open('cientista.txt', 'r') as arquivo:
    conteudo = arquivo.read()
#printando o tamanho da string do objeto
print(len(conteudo))
#printando conteudo
print(conteudo)
print('')

#fatiando o conteudo do arquivo
#abrindo para o modo escrita
with open('cientista.txt', 'w') as arquivo:
    #sobescrevendo 21 caracteres da variavel texto no arquivo passado
    arquivo.write(texto[:21])
    #escrevendo uma quebra de linha no arquivo
    arquivo.write('\n')
    #sobescrevendo 33 caracteres da variavel texto no arquivo passado
    arquivo.write(texto[:33])

#lendo o arquivo
arquivo = open('cientista.txt', 'r')
#passando arquivo para objeto
conteudo = arquivo.read()
#fechando arquivo
arquivo.close()
#imprimindo conteudo do arquivo
print(conteudo)
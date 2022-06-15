#  Created by avivyh on 09/06/22.
#  Copyright © 2022  avivyh. All rights reserved.

''' MANIPULAÇÃO DE ARQUIVOS CSV '''
#csv significa : arquivos separados por virgula

#importando pacote para manipular arquivos csv
import csv

#abrindo pacote para escrita
# o with fecha automaticamente o arquivo
with open('numeros.csv', 'w') as arquivo:
    #csv é o pacote, writer é uma função, o arquivo passado como parametro para alteração
    writer = csv.writer(arquivo)
    #comando para escrever na linha 
    writer.writerow(('primeira', 'segunda', 'terceira'))
    writer.writerow((12, 13, 14))
    writer.writerow((15, 16, 17))

#fazendo leitura de arquivos csv
with open('numeros.csv', 'r') as arquivo:
    #csv é o pacote, reader é a função para leitura, o arquivo é passado como parametro
    leitor = csv.reader(arquivo)
    for x in leitor:
        print('numero de colunas : ', len(x))
        print(x)
print('')

#gerando uma lista com dados do arquivo csv
with open('numeros.csv', 'r') as arquivo:
    #passando o conteudo do arquivo para a variavel leitor
    leitor = csv.reader(arquivo)
    #convertendo o conteudo do arquivo para uma lista
    dados = list(leitor)
#printando a lista
print(dados)

#imprimindo a partir da segunda linha 
for linha in dados[:1]:
    print(linha)
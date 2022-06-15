#  Created by avivyh on 15/06/22.
#  Copyright © 2022  avivyh. All rights reserved.
"""Manipulação de arquivos JSON

JAVASCRIPT OBJECT NOTATION

"""

#criando UM DICIONÁRIO
dic = {'nome': 'Vivyh', 'linguagem': 'Python', 'similar': ['c', 'c++', 'lisp'], 'users': 1000000}

#imprimindo todos os itens 
for k, v in dic.items():
    print(k, v)
print('')

#importando modulo json
import json

#convertendo o dicionário para um objeto json
json.dumps(dic)

#criando arquivo json para escrita
with open('dados.json', 'w') as arquivo:
    #escrevendo arquivos do dicionário no arquivo
    arquivo.write(json.dumps(dic))

#abrindo arquivo json para leitura
with open('dados.json', 'r') as arquivo:
    #gravando na variavel texto
    texto = arquivo.read()
    data = json.loads(texto)
print(data)
print('')

#acessando valor no dicionário a partir da chave 
print(data['nome'])
print('')

#imprimindo um arquivo json copiado da internet
from urllib.request import urlopen

#a variavel response recebe a função urlopen, passa o link como parametro
#é feito o read e depois o decode para utf8
response = urlopen('http://vimeo.com/api/v2/video/57733101.json').read().decode('utf8')
#gravando o conteudo do objeto response no objeto data
#a função loads é para carregar o conteudo
data = json.loads(response)[0]
print('Título:', data['title'])
print('URL: ', data['url'])
print('Duração: ', data['duration'])
print('Número de visualizações: ', data['stats_number_of_plays'])
print('')


#copiando o conteúdo de um arquivo para o outro
#importando pacote os
import os
arquivoFonte = 'dados.json'
arquivoDestino = 'jsondata.txt'

#método 1:
#abrir um arquivo e automaticamente copiar o conteudo para o outro arquivo
with open(arquivoFonte, 'r') as infile:
    #variavel texto recebe a leitura do arquivo
    texto = infile.read()
    #abrindo arquivo de destino para escrita
    with open(arquivoDestino, 'w') as outfile:
        outfile.write(texto)

#método 2:
#abre o arquivo de destino para escrita
#abrindo arquivo fonte para leitura
open(arquivoDestino, 'w').write(open(arquivoFonte, 'r').read())

#leitura de arquivos json
with open('jsondata.txt', 'r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

print(data)
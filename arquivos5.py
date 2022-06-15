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

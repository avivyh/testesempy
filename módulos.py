"""
MÓDULOS EM PYTHON SÃO ARQUIVOS PYTHON COM A EXTENSÃO .py QUE IMPLEMENTAM UM CONJUNTO DE FUNÇÕES 
IMPORTAMOS O MÓDULO EM NOSSO SCRIPT USANDO O COMANDO IMPORT

ex:
    import math

A PRIMEIRA VEZ QUE UM MÓDULO É CARREGASO EM SCRIPT PYTHON ELE É
INICIALIZADO E FICA DISPONÍVEL PARA USO.

UM MÓDULO SÓ PRECISA SER IMPORTADO UMA VEZ NO CÓDIGO.

ESCREVER MÓDULOS PYTHON É MUITO SIMPLES. PARA CRIAR UM MÓDULO DE 
SUA PREFERENCIA, BASTA CRIAR UM NOVO ARQUIVO .py COM O NOME DO MÓDULO
E, EM SEGUIDA, IMPORTÁ - LO UTILIZANDO O COMANDO DE IMPORTAÇÃO.

ex: 
    meu_modulo.py
    import"meu_modulo"

TAMBÉM É POSSÍVEL IMPORTAR FUNÇÕES ESPECIFICAS DE UM MÓDULO

#importando a função sqrt do módulo math
from math import sqrt

ISSO ECONOMIZA MEMORIA

"""

''' 

PACOTES SÃO UMA FORMA DE ESTRUTURAR OS MÓDULOS EM PYTHON

import modulo
import pacote.modulo

UM PACOTE É UM CONJUNTO DE MODULOS PYTHON

ENQUANTO UM MÓDULO É UM ÚNICO ARQUIVO PYTHON, UM PACOTE É UM DIRETÓRIO
DE MÓDULOS PYTHON CONTENDO UM ARQUIVO __init__.py

'''

#importando um módulo
import math

#verificando todos os métodos disponíveis no módulo
print(dir(math))
print('')

#usando um dos métodos do módulo math
#chama a função, antes do ponto fica o nome do pacote. 
print(math.sqrt(25))
print('')

#importando apenas um dos métodos do módulo math
from math import sqrt
#usando o método importado
print(sqrt(9))
print('')

#imprimindo todos o métodos do módulo math
print(dir(math))

#help para comandos de um método, o comando mostra exatamente
#para que serve uma função
help(sqrt)


#importando outro pacote
import random
#chamando metodo choice a partir do pacote random
print(random.choice(['Maça', 'Banana', 'Laranja']))

#gerando amostra aleatoria a partir de um conjunto de dados
print(random.sample(range(100), 10))
print('')


#importando módulo
import statistics
dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

#calculando a media da lista
print(statistics.mean(dados))
print('')

#calculando a mediana
print(statistics.median(dados))
print('')

#importando módulo os (para operações do sistema operacional)
import os
#chamando função para saber em qual diretório estou agora
print(os.getcwd())
print('')

#para saber todos os métodos que o módulo os oferece
print(dir(os))
print('')

#pacote sys permite interagir com o sistema operacional
import sys
#imprimindo teste no terminal 
print(sys.stdout.write('Teste'))
print('')
#descobrindo a versão do interpretador
print(sys.version)
print('')

#importando o módulo request do pacote urllib, usado para trazer
# url's para dentro do ambiente python
import urllib.request

#variável resposta armazena o objeto de conexão à url passada
#como parametro
#função urlopen
resposta = urllib.request.urlopen('http://python.org')
print(resposta)
print('')

#chamando o método read do objeto resposta e armazenando
#código html na variavel html
html = resposta.read()

#imprimindo html 
print(html)
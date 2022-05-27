#dicionários em python
"""
Os dicionários são construídos com o uso de chaves e virgulas separando cada elemento do dicionário
dict = {k1:v1, k2: v2, ... kn:vn}

"""
#criando lista
Lista = ['Fernanda', 22, 'Matheus', 24, 'Lucas', 21, 'Laís', 27]
print(Lista)

#criando dicionários
Dcnr = {'Fernanda':22, 'Matheus':24, 'Lucas':21, 'Laís':27}
print(Dcnr)

#printando o valor armazenado em uma chave especifica
print(Dcnr['Matheus'])

#adicionando mais um mapeamento
Dcnr['Pedro'] = 23
print(Dcnr)

#excluindo dados do dicionário
Dcnr.clear()
print(Dcnr)

#deletar o dicionário 
del Dcnr

#criando dicionário
Estudantes = {'Ana':21, 'Caio':22, 'Lucas':23, 'Fernando':24, 'Alexandre':14}

#verificando o tamanho do dicionário
print(Estudantes)
#Cada combinação de chave e elemento equivale a 1 no comprimento
print(len(Estudantes))

#extraindo as chaves do dicionário
print(Estudantes.keys())
#extraindo os valores do dicionário
print(Estudantes.values())
#printando todos os itens
print(Estudantes.items())
print('')
Estudantes2 = {'Maria':22, 'Karla':21, 'Nilton':20}
print(Estudantes2)
print('')

#concatenando dicionários
Estudantes.update(Estudantes2)
print(Estudantes)

#criando dicionário vazio
Dici = {}

#adicionando elementos no dicionário
Dici['primeira chave'] = 1
print(Dici)
print('')
#é possível adicionar elementos com tipos de chave diferentes
Dici[20] = 2
print(Dici)
print('')
#os valores também podem ser de tipos diferentes
Dici[30] = 'Python'
print(Dici)
print('')
Dici['Teste'] = 5
print(Dici)
print('')

#criando dicionário vazio 
dic = {}
print(dic)
#atribuindo valor
dic['One'] = 5
print(dic)
dic['Two'] = 6
print(dic)
print('')

#criando novo dicionário
newdi = {}
#atribuindo valores
newdi['OneKey'] = 'Big Day'
print(newdi)
newdi['TwoKey'] = 27
print(newdi)
newdi['TreeKey'] = 5
print(newdi)
newdi['FourKey'] = 2022
print(newdi)
print('')

#passando os valores das chaves para variáveis
a = newdi['OneKey']
b = newdi['TwoKey']
print(a, b)
print('')

#criando dicionário de listas
dicionario = {'chave1':[1, 2, 3], 'chave2':[4, 5, 6], 'chave3':[7, 8, 9]}
print(dicionario)
print(dicionario['chave1'])
print('')

#acessando um valor da lista, de dentro do dicionário
print(dicionario['chave1'][0])
#atribuindo valor diferente para um item da lista de dentro do dicionário
dicionario['chave1'][0] = 'chocolate'
print(dicionario['chave1'][0])
print(dicionario)
print('')

#printando em maiúsculo o item da lista, dentro do dicionário
print(dicionario['chave1'][0].upper())
print('')

#variaveis podem realizar operações com valores de dentro de um dicionário
var = dicionario['chave3'][2] - 2
print(var)
#também podemos realizar operações dentro de uma lista que está em um dicionário
dicionario['chave3'][2] -= 2
print(dicionario)
print('')

#criando dicionário dentro de outro dicionário
Dix = {'Chave1':{'Chave2Valor1':{'Chave3': 'ValorArmazenado'}}}
print(Dix)

#acessando item 
print(Dix['Chave1']['Chave2Valor1']['Chave3'])
print('')
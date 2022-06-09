#importando pandas que é um conjunto de um pacote para analise de dados
import pandas as pd
#passando nome do arquivo para variavel filename
fileName = 'binary.csv'
#fazendo a leitura do arquivo para dentro de um objeto
df = pd.read_csv(fileName)
#imprimindo apenas as primeiras linhas (ou seja, a caeça do arquivo)
print(df.head())

#abrindo arquivo com pandas 
#passando nome do arquivo para variável
file2 = 'salarios.csv'
#fazendo a leitura de um arquivo pra dentro de um objeto
df2 = pd.read_csv(file2)
#printando o arquivo
print(df2.head())